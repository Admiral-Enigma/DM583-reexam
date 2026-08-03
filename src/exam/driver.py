"""One-shot driver for the geometric Q2/Q6-style questions.

  >>> res = analyze("A 5 2 / B 1 7 / C 3 3", metric="man", k=2, db=(3, 2))
  >>> check_order("C,A,B", res["lof"])
"""
from .dist import eucd, mand, supd
from .outliers import knn_outlier, wknn_outlier, lof_table
from .cluster import dbscan

METRICS = {"man": mand, "euc": eucd, "sup": supd}

def parse(text: str) -> tuple[list[str], list[list[float]]]:
  """
  Parse labeled points pasted as 'A 5 2 / B 1 7 / ...' (slashes or newlines
  between points; commas allowed inside). Rows without a leading label get
  A, B, C, ... Returns (labels, points).
  """
  rows = [r.replace(",", " ").split() for r in text.replace("/", "\n").splitlines() if r.split()]
  labels, pts = [], []
  for i, r in enumerate(rows):
    try:
      float(r[0])
      lab, vals = chr(ord("A") + i), r
    except ValueError:
      lab, vals = r[0], r[1:]
    labels.append(lab)
    pts.append([float(x) for x in vals])
  return labels, pts

def print_matrix(D, labels) -> None:
  "Print a labeled distance matrix."
  w = max(7, max(len(l) for l in labels) + 2)
  print(" " * w + "".join(l.rjust(w) for l in labels))
  for l, row in zip(labels, D):
    print(l.rjust(w) + "".join(f"{v:{w}.4g}" for v in row))

def analyze(text, metric="euc", k: int | None = None, db=None) -> dict:
  """
  Everything for a geometric question in one shot.
  text: 'A 5 2 / B 1 7 / ...' (or a (labels, points) pair).
  metric: 'man' | 'euc' | 'sup' (or a distance function).
  k: also print kNN outlier scores (dist-to-kth + weighted) and the LOF table.
  db: (eps, minpts) or [(eps, minpts), ...]: also run DBSCAN for each setting.
  Returns dict: D, and per-label score dicts 'knn', 'wknn', 'lrd', 'lof',
  'dbscan(eps,minpts)' — feed those into check_order().
  """
  labels, pts = parse(text) if isinstance(text, str) else text
  d = METRICS[metric] if isinstance(metric, str) else metric
  mname = metric if isinstance(metric, str) else d.__name__
  D = [[d(a, b) for b in pts] for a in pts]
  print(f"n={len(pts)}  metric={mname}")
  print_matrix(D, labels)
  res = {"labels": labels, "points": pts, "D": D}
  if k is not None:
    ks, ws = knn_outlier(pts, k, d), wknn_outlier(pts, k, d)
    res["knn"], res["wknn"] = dict(zip(labels, ks)), dict(zip(labels, ws))
    print(f"\nkNN outlier scores (k={k}):")
    for l, a, b in zip(labels, ks, ws):
      print(f"  {l}: dist-to-kth (k={k}) = {a:g}   weighted (avg of 1..{k}) = {b:g}")
    print(f"\nLOF pipeline (k={k}):")
    lrds, lofs = lof_table(pts, k, d, labels)
    res["lrd"], res["lof"] = dict(zip(labels, lrds)), dict(zip(labels, lofs))
  if db is not None:
    for eps, mp in [db] if isinstance(db, tuple) else db:
      cl, typ = dbscan(pts, eps, mp, d)
      print(f"\nDBSCAN eps={eps:g} MinPts={mp} (point counts itself):")
      groups: dict[int, list[str]] = {}
      for l, c in zip(labels, cl):
        groups.setdefault(c, []).append(l)
      for c in sorted(groups):
        print(f"  {'noise' if c == 0 else f'cluster {c}'}: {groups[c]}")
      print("  types: " + "  ".join(f"{l}:{t}" for l, t in zip(labels, typ)))
      res[f"dbscan({eps:g},{mp})"] = dict(zip(labels, zip(cl, typ)))
  return res

def cheat() -> None:
  "Print the one-line usage map for every exam tool (use help(fn) for details)."
  print("""\
GEOMETRIC (Q2/Q6): res = analyze("A 5 2 / B 1 7 / ...", metric="man"|"euc"|"sup", k=2, db=(2, 6))
                   -> prints dist matrix, kNN scores, LOF table, DBSCAN; returns score dicts
  ordering sub:    check_order("C,D,E", res["lof"])   or res["knn"]
DBSCAN (Q6):       analyze("A 2 4 / B 4 4 / ...", "man", db=[(2, 6), (2, 4), (2, 2)])
                   -> one run per (eps, MinPts) sub: clusters + core/border/noise per point
                   (point counts itself; res["dbscan(2,6)"]["S"] -> (cluster_id, "border"))
DENSITY (Q1):      discrete_kernel(data, x=4, h=1)    knn_density(data, x=7, k=2)
  one shot:        density_report(data, [("kernel", 4, 1), ("knn", 7, 2)])
AHC (Q4):          D = proxmat(pts, mand)  or paste the matrix as list of rows
                   ahc_all(D, labels=["1","2","3","4","5"])
  figure match:    match_dendrogram(D, [2, 6, 8, 10])     # scale verdict per linkage
  cut at level:    cut_height(D, "single", 4, labels=[...])
APRIORI (Q5/Q8):   db = parse_db("A,B,C,D / A,C,D,F / ...")
                   apriori(db, 3)                 # levels: join -> prune(named) -> counts
                   prunable(("B","C","D","E"), [("A","B","C"), ...])   # Q5 in one call
                   rule(db, "AD", "C")            # supp count, rel, conf fraction, lift
                   conf_compare(db, "AD", "C", moved="D")   # conf monotonicity (Q8.1)
SIMILARITY (Q3):   dist_compare([[1,2],[2,1]])    # Mah vs Euc/Man/Sup per point + PSD check
                   binary_compare([1,1,0], [1,0,1], pad=20)   # SMC vs Jaccard vs cosine, 0-0 effect
GMM (Q7):          mstep1d(xs, gammas)            # gammas rows=points: [[.9,.1], ...]
                   hard_partition(gammas)         param_count(k=2, d=1)
                   check_claim("mu1", computed, 14.2/3.8)
K-MEANS (Q9):      data = dict(A=2, B=4, ...)
                   kmeans_trace(data, [2, 4.5, 6])          # iterations + final clusters
                   analyze_partitions(data, {"P1": [["A","B"], ...]}, compare_point="A")
RULES: answer only what a tool printed. Recall < 75% sure -> BLANK. help(fn) for details.""")

def check_order(order: str, scores: dict, strict: bool = False) -> bool:
  """
  Is this subset correctly ordered by score, non-strictly decreasing (the exact
  form of the Q2 subs)? order: 'C,D,E' or 'C>D>E'; scores: label->score dict
  (e.g. res['lof'] from analyze). Also prints the full ranking.
  """
  seq = [s.strip() for s in order.replace(">", ",").split(",")]
  vals = [scores[s] for s in seq]
  ok = all((a > b) if strict else (a >= b - 1e-12) for a, b in zip(vals, vals[1:]))
  print("  claimed order: " + "  ".join(f"{s}={v:.4f}" for s, v in zip(seq, vals)))
  full = sorted(scores, key=lambda l: -scores[l])
  print("  full ranking:  " + " >= ".join(f"{l}({scores[l]:.4f})" for l in full))
  print(f"  => {'OK: non-increasing' if ok else 'WRONG ORDER'}")
  return ok
