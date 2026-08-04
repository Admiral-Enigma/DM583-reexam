from .dist import Vector, Matrix, eucd

# ---------- k-Means / partitioning ----------

def centroid(pts: Matrix) -> list[float]:
  "Mean vector (centroid) of a set of points."
  return [sum(c)/len(pts) for c in zip(*pts)]

def sse(data: Matrix, labels: Vector, cents: Matrix) -> float:
  "Sum of Squared Errors of a partition (k-Means objective)."
  return sum(eucd(data[i], cents[labels[i]])**2 for i in range(len(data)))

def kmeans(data: Matrix, init: Matrix, iters: int = 100) -> tuple[list[int], Matrix]:
  """
  k-Means with squared Euclidean distance and given initial prototypes.
  Returns (labels, centroids). Iterates assign/update until stable.
  """
  cents = [list(c) for c in init]
  labels = [0]*len(data)
  for _ in range(iters):
    new = [min(range(len(cents)), key=lambda c: eucd(x, cents[c])) for x in data]
    if new == labels: break
    labels = new
    cents = [centroid([data[i] for i in range(len(data)) if labels[i] == c]) or cents[c]
             for c in range(len(cents))]
  return labels, cents

def silhouette(data: Matrix, labels: Vector, d=eucd) -> float:
  """
  Average Silhouette Width (SWC) in [-1,1]. Uses full pairwise distances.
  a(i)=avg dist to own cluster; b(i)=min avg dist to another cluster.
  """
  ss = []
  for i in range(len(data)):
    same = [j for j in range(len(data)) if labels[j] == labels[i] and j != i]
    if not same: ss.append(0.0); continue
    a = sum(d(data[i], data[j]) for j in same)/len(same)
    other = set(labels) - {labels[i]}
    b = min(sum(d(data[i], data[j]) for j in range(len(data)) if labels[j] == c)
            / sum(1 for j in range(len(data)) if labels[j] == c) for c in other)
    ss.append((b-a)/max(a, b))
  return sum(ss)/len(ss)

def simp_silhouette(data: Matrix, labels: Vector, d=eucd, verbose: bool = True) -> list[float]:
  """
  SIMPLIFIED silhouette per point (centroid-based, what the exam asks per observation):
  a(i) = d(i, own centroid), b(i) = min d(i, other centroid), s = (b-a)/max(a,b).
  Returns [s(i)]. NB: a singleton cluster gets a=0 => s=1 under this definition.
  """
  cl = sorted(set(labels))
  cents = {c: centroid([data[i] for i in range(len(data)) if labels[i] == c]) for c in cl}
  ss = []
  for i in range(len(data)):
    a = d(data[i], cents[labels[i]])
    b = min(d(data[i], cents[c]) for c in cl if c != labels[i])
    s = 0.0 if max(a, b) == 0 else (b-a)/max(a, b)
    ss.append(s)
    if verbose:
      print(f"  i={i} x={list(data[i])} cluster={labels[i]}  a={a:.4f}  b={b:.4f}  s=(b-a)/max(a,b)={s:.4f}")
  if verbose:
    print(f"  mean simplified silhouette = {sum(ss)/len(ss):.4f}")
  return ss

def _named_1d(data) -> dict[str, tuple]:
  """Accept {'A': 2}, {'A': (1, 2)}, or a plain list (auto-named A, B, C, ...).
  Values are normalised to tuples, so every helper works in any dimension."""
  if not isinstance(data, dict):
    data = {chr(ord("A") + i): v for i, v in enumerate(data)}
  return {k: tuple(v) if isinstance(v, (list, tuple)) else (v,)
          for k, v in data.items()}

def _vmean(cl, data):
  return tuple(sum(data[p][d] for p in cl)/len(cl) for d in range(len(next(iter(data.values())))))

def _vd(a, b):
  return sum((x - y)**2 for x, y in zip(a, b))**.5

def _vfmt(v):
  return round(v[0], 4) if len(v) == 1 else tuple(round(x, 4) for x in v)

def kmeans_trace(data, init, max_iter: int = 50, verbose: bool = True):
  """
  k-Means (Lloyd) with NAMED points and the full trace shown — for the
  'converges in exactly N iterations' subs (June Q9.1). Works in 1-D or n-D:
  data: {'A': 2, ...} or {'A': (1, 2), ...} or a list; init: initial centroids
  (scalars in 1-D, tuples in n-D). One iteration = assign all points, then
  update centroids. Returns (clusters, n_changing_iterations); the run stops
  when an iteration reproduces the previous assignment.
  """
  data = _named_1d(data)
  cents = [tuple(c) if isinstance(c, (list, tuple)) else (c,) for c in init]
  prev = None
  if verbose:
    print(f"k-means from centroids {[_vfmt(c) for c in cents]}:")
  for it in range(1, max_iter + 1):
    assign = {p: min(range(len(cents)), key=lambda j: _vd(v, cents[j]))
              for p, v in data.items()}
    clusters = [sorted(p for p in data if assign[p] == j) for j in range(len(cents))]
    cents = [_vmean(cl, data) if cl else cents[j] for j, cl in enumerate(clusters)]
    if verbose:
      print(f"  iter {it}: {clusters} -> centroids {[_vfmt(c) for c in cents]}")
    if clusters == prev:
      if verbose:
        print(f"  converged: {it - 1} iteration(s) changed the assignment "
              f"(iter {it} confirmed no change).")
      return clusters, it - 1
    prev = clusters
  if verbose: print("  did NOT converge within max_iter")
  return prev, max_iter

def silhouette_point(data, partition, point, verbose: bool = True):
  """
  BOTH silhouettes of one named observation (Exercise 3-5 style):
  full SWC   : a = avg dist to OTHER members of own cluster,
               b = min over other clusters of avg dist to their members;
  simplified : a = dist to own centroid, b = min dist to another centroid.
  data: {'A': 2 or (x, y), ...}; partition: list of name-lists.
  Returns (s_full, s_simplified).
  """
  data = _named_1d(data)
  own = next(cl for cl in partition if point in cl)
  others = [cl for cl in partition if point not in cl]
  mates = [p for p in own if p != point]
  a_f = sum(_vd(data[point], data[p]) for p in mates)/len(mates) if mates else 0.0
  bs_f = {tuple(cl): sum(_vd(data[point], data[p]) for p in cl)/len(cl) for cl in others}
  b_f = min(bs_f.values())
  s_f = 0.0 if max(a_f, b_f) == 0 else (b_f - a_f)/max(a_f, b_f)
  a_s = _vd(data[point], _vmean(own, data))
  bs_s = {tuple(cl): _vd(data[point], _vmean(cl, data)) for cl in others}
  b_s = min(bs_s.values())
  s_s = 0.0 if max(a_s, b_s) == 0 else (b_s - a_s)/max(a_s, b_s)
  if verbose:
    print(f"silhouettes of {point} (own cluster {sorted(own)}):")
    print(f"  FULL:       a = avg dist to own mates = {a_f:.4f}")
    for cl, b in bs_f.items():
      print(f"              avg dist to {sorted(cl)} = {b:.4f}")
    print(f"              b = {b_f:.4f}  ->  s = (b-a)/max(a,b) = {s_f:.5f}")
    print(f"  SIMPLIFIED: a = dist to own centroid = {a_s:.4f}")
    for cl, b in bs_s.items():
      print(f"              dist to centroid of {sorted(cl)} = {b:.4f}")
    print(f"              b = {b_s:.4f}  ->  s = {s_s:.5f}")
    if len(own) == 1:
      print("              (singleton: a = 0 -> s = 1 under both definitions)")
  return s_f, s_s

def is_fixed_point(data, partition, verbose: bool = True) -> bool:
  """
  Would Lloyd's reassignment step change this 1-D partition? True = k-Means is
  trapped here if it ever arrives (June Q9.2). partition: list of name-lists.
  """
  data = _named_1d(data)
  cents = [_vmean(cl, data) for cl in partition]
  stable = True
  for i, cl in enumerate(partition):
    for p in cl:
      best = min(range(len(cents)), key=lambda j: _vd(data[p], cents[j]))
      if _vd(data[p], cents[best]) < _vd(data[p], cents[i]) - 1e-12:
        stable = False
        if verbose:
          print(f"  {p} would move: d({_vfmt(data[p])}, {_vfmt(cents[i])}) > "
                f"d({_vfmt(data[p])}, {_vfmt(cents[best])})")
  if verbose: print(f"  fixed point of Lloyd's algorithm: {stable}")
  return stable

def analyze_partitions(data, partitions: dict, compare_point: str | None = None) -> dict:
  """
  June-Q9 in one shot. data: {'A': 2, ...}; partitions: {'P1': [['A','B'], ...]}.
  Per partition: per-cluster centroid + SSE, fixed-point check. Then a ranking
  that flags stable-but-not-best traps, and (optionally) the simplified
  silhouette of one named point compared across all partitions.
  Returns {name: (sse, stable)}.
  """
  data = _named_1d(data)
  results = {}
  for name, part in partitions.items():
    print(f"--- {name}: {part}")
    total = 0.0
    for cl in part:
      c = _vmean(cl, data)
      s = sum(_vd(data[p], c)**2 for p in cl)
      total += s
      print(f"  {sorted(cl)}: centroid {_vfmt(c)}, SSE {s:.4g}")
    print(f"  total SSE = {total:.4g}")
    stable = is_fixed_point(data, part)
    results[name] = (total, stable)
    print()
  best = min(results, key=lambda n: results[n][0])
  for name, (s, stable) in results.items():
    tag = "  <- LOWEST SSE" if name == best else ""
    trap = "  ** stable local minimum, NOT best -> k-Means trap **" \
        if stable and name != best else ""
    print(f"{name}: SSE {s:.4g}, fixed point {stable}{tag}{trap}")
  if compare_point:
    print(f"\nsimplified silhouette of {compare_point}:")
    for name, part in partitions.items():
      cents = [_vmean(cl, data) for cl in part]
      own = next(i for i, cl in enumerate(part) if compare_point in cl)
      a = _vd(data[compare_point], cents[own])
      b = min(_vd(data[compare_point], cents[i]) for i in range(len(cents)) if i != own)
      s = 0.0 if max(a, b) == 0 else (b - a)/max(a, b)
      single = "   (singleton: a=0 -> s=1)" if len(part[own]) == 1 else ""
      print(f"  in {name}: a = {a:.4g}, b = {b:.4g} -> s = {s:.4f}{single}")
  return results

# ---------- agglomerative hierarchical ----------

def pairmat(text: str, verbose: bool = True):
  """
  Build a square distance matrix from PAIRWISE distances pasted straight from
  an exam sheet, e.g.:
      pairmat("d(1,2)=4 d(1,3)=10 d(1,4)=20 d(1,5)=18 d(2,3)=8 "
              "d(2,4)=18 d(2,5)=16 d(3,4)=12 d(3,5)=14 d(4,5)=6")
  Any separators work — numbers are read in triples (i, j, distance), labels
  1-based. Returns (D, labels) ready for ahc_all / match_dendrogram / cut_height.
  """
  import re
  nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text)]
  if len(nums) % 3:
    raise ValueError(f"read {len(nums)} numbers — not divisible into (i, j, d) triples")
  triples = [(int(nums[k]), int(nums[k+1]), nums[k+2]) for k in range(0, len(nums), 3)]
  n = max(max(i, j) for i, j, _ in triples)
  D = [[0.0]*n for _ in range(n)]
  seen = set()
  for i, j, d in triples:
    D[i-1][j-1] = D[j-1][i-1] = d
    seen.add(frozenset((i, j)))
  missing = [(i, j) for i in range(1, n+1) for j in range(i+1, n+1)
             if frozenset((i, j)) not in seen]
  if missing:
    print(f"  WARNING: {len(missing)} pair(s) missing (left as 0): {missing}")
  labels = [str(i) for i in range(1, n+1)]
  if verbose:
    print(f"n = {n}, {len(triples)} pairs (expected {n*(n-1)//2})")
    for l, row in zip(labels, D):
      print(f"  {l}: {[round(x, 4) if x % 1 else int(x) for x in row]}")
  return D, labels

def sqmat(text: str, verbose: bool = True):
  """
  Parse a SQUARE distance matrix pasted row by row (rows split on '/' or
  newlines), e.g. June 2026 Q4:
      sqmat("0 2 14 22 18 / 2 0 10 18 16 / 14 10 0 8 10 / 22 18 8 0 6 / 18 16 10 6 0")
  Validates: square, zero diagonal, symmetric — and reports any violation
  (the transcription guard). Returns (D, labels) with labels '1'..'n'.
  """
  rows = [[float(x) for x in r.replace(",", " ").split()]
          for r in text.replace("/", "\n").splitlines() if r.split()]
  n = len(rows)
  bad = [len(r) for r in rows if len(r) != n]
  if bad:
    raise ValueError(f"{n} rows but row lengths {[len(r) for r in rows]} — not square")
  for i in range(n):
    if rows[i][i] != 0:
      print(f"  WARNING: diagonal D[{i+1}][{i+1}] = {rows[i][i]:g}, expected 0 — typo?")
    for j in range(i+1, n):
      if rows[i][j] != rows[j][i]:
        print(f"  WARNING: D[{i+1}][{j+1}] = {rows[i][j]:g} but D[{j+1}][{i+1}] = "
              f"{rows[j][i]:g} — not symmetric, typo?")
  labels = [str(i) for i in range(1, n+1)]
  if verbose:
    print(f"{n}x{n} matrix OK" if not bad else "")
    for l, r in zip(labels, rows):
      print(f"  {l}: {[int(x) if not x % 1 else x for x in r]}")
  return rows, labels

AHC_METHODS = ("single", "complete", "average", "ward")

def ahc(D: Matrix, method: str = "single") -> list[tuple]:
  """
  Agglomerative hierarchical clustering from distance matrix D.
  method in {single, complete, average, ward}. Ward uses the Lance-Williams
  recursion on SQUARED distances (matches scipy for Euclidean input).
  Returns merges [(clusterA, clusterB, height), ...] in order;
  clusters are tuples of original 0-based indices.
  """
  act = [(i,) for i in range(len(D))]
  key = lambda a, b: (a, b) if a <= b else (b, a)
  dist = {key(a, b): D[a[0]][b[0]] for a in act for b in act if a < b}
  merges = []
  while len(act) > 1:
    (a, b), h = min(dist.items(), key=lambda kv: kv[1])
    merges.append((a, b, h))
    new = tuple(sorted(a+b))
    for c in [x for x in act if x not in (a, b)]:
      da, db = dist[key(a, c)], dist[key(b, c)]
      if method == "single":   dnew = min(da, db)
      elif method == "complete": dnew = max(da, db)
      elif method == "average":  dnew = (len(a)*da + len(b)*db)/(len(a)+len(b))
      elif method == "ward":
        s = len(a)+len(b)+len(c)
        dnew = (((len(a)+len(c))*da**2 + (len(b)+len(c))*db**2
                 - len(c)*dist[key(a, b)]**2)/s)**.5
      dist[key(new, c)] = dnew
    act = [x for x in act if x not in (a, b)] + [new]
    dist = {k: v for k, v in dist.items() if a not in k and b not in k}
  return merges

def cut(merges: list[tuple], n: int, k: int) -> list[set]:
  "Cut a hierarchy (n points) to get k clusters from the merge list."
  cl = [{i} for i in range(n)]
  for a, b, _ in merges:
    if len(cl) <= k: break
    A = next(c for c in cl if set(a) <= c)
    B = next(c for c in cl if set(b) <= c)
    cl.remove(A); cl.remove(B); cl.append(A | B)
  return cl

def cut_height(D: Matrix, method: str, h: float, labels=None) -> list[tuple]:
  """
  Horizontal cut of the dendrogram at level h: only merges with height < h
  have happened (June Q4.5: cut at 4 -> merge@6 has NOT happened). A merge at
  exactly h is flagged as convention-dependent and treated as NOT merged.
  Returns the clusters as sorted tuples of indices (or labels).
  """
  merges = ahc(D, method)
  parent = {i: frozenset({i}) for i in range(len(D))}
  for a, b, hh in merges:
    if abs(hh - h) < 1e-12:
      print(f"  NOTE: merge {a}+{b} at exactly h={h:g} — convention-dependent; "
            f"treating as NOT merged (strict <).")
    if hh < h - 1e-12:
      merged = parent[a[0]] | parent[b[0]]
      for i in merged: parent[i] = merged
  name = (lambda i: labels[i]) if labels else (lambda i: i)
  clusters = sorted({tuple(sorted(name(i) for i in c)) for c in parent.values()},
                    key=lambda t: [str(x) for x in t])
  print(f"cut {method} @ {h:g}: {[list(c) for c in clusters]}")
  return clusters

def _fmt_cl(c, labels=None) -> str:
  return "{" + ",".join(labels[i] if labels else str(i) for i in c) + "}"

def ahc_all(D: Matrix, labels=None, methods=AHC_METHODS) -> dict[str, list[tuple]]:
  """
  Run AHC with every linkage; print each merge sequence with heights, then the
  height lists side by side (+ scipy cross-check if available). Returns {method: merges}.
  """
  out = {}
  for m in methods:
    out[m] = ahc(D, m)
    print(f"\n{m}:")
    for s, (a, b, h) in enumerate(out[m], 1):
      print(f"  {s}. {_fmt_cl(a, labels)} + {_fmt_cl(b, labels)}   h = {h:g}")
  print("\nmerge heights:")
  for m in methods:
    print(f"  {m:<9} {[round(h, 4) for *_, h in out[m]]}")
  try:
    import numpy as np
    from scipy.spatial.distance import squareform
    from scipy.cluster.hierarchy import linkage
    cond = squareform(np.array(D), checks=False)
    print("scipy cross-check:")
    for m in methods:
      print(f"  {m:<9} {[round(float(h), 4) for h in linkage(cond, m)[:, 2]]}")
  except ImportError:
    pass
  return out

def match_dendrogram(D: Matrix, heights: Vector, labels=None, merges=None,
                     tol: float = 1e-6, methods=AHC_METHODS) -> dict[str, tuple]:
  """
  Does a dendrogram with the given merge heights (e.g. [2, 6, 8, 10]) correspond
  to each linkage on D?  scale match = computed heights equal `heights`;
  topology match (only checked if `merges` is given as an ordered list of pairs of
  index-tuples, e.g. [((0,),(1,)), ((0,1),(2,))]) = same clusters merged per step.
  "Corresponds to X-linkage" requires BOTH. Returns {method: (topology, scale)}.
  """
  res = {}
  want_h = sorted(heights)
  for m in methods:
    mg = ahc(D, m)
    hs = sorted(h for *_, h in mg)
    scale = len(hs) == len(want_h) and all(abs(a-b) <= tol for a, b in zip(hs, want_h))
    topo = None
    if merges is not None:
      want_t = [frozenset((frozenset(a), frozenset(b))) for a, b in merges]
      got_t = [frozenset((frozenset(a), frozenset(b))) for a, b, _ in mg]
      topo = got_t == want_t
    res[m] = (topo, scale)
    seq = "  ".join(f"{_fmt_cl(a, labels)}+{_fmt_cl(b, labels)}@{h:g}" for a, b, h in mg)
    t = {None: "n/a (pass merges=...)", True: "YES", False: "NO"}[topo]
    verdict = "CORRESPONDS" if scale and topo else \
              "does NOT correspond" if scale is False or topo is False else "heights match, topology unchecked"
    print(f"{m:<9} heights {[round(h,4) for h in hs]} vs claimed {want_h} -> scale {'YES' if scale else 'NO'}; topology {t}")
    print(f"          {seq}")
    print(f"          => {verdict}")
  return res

# ---------- DBSCAN ----------

def dbscan(data: Matrix, eps: float, minpts: int, d=eucd) -> tuple[list[int], list[str]]:
  """
  DBSCAN. Returns (labels, types). label 0 = noise, else cluster id (1..k);
  types[i] in {core, border, noise}. Core counts the point itself within eps.
  """
  n = len(data)
  nb = [[j for j in range(n) if d(data[i], data[j]) <= eps] for i in range(n)]
  core = {i for i in range(n) if len(nb[i]) >= minpts}
  labels, cid = [0]*n, 0
  for i in core:
    if labels[i]: continue
    cid += 1; stack = [i]
    while stack:
      p = stack.pop()
      if labels[p] == 0: labels[p] = cid
      if p in core:
        for q in nb[p]:
          if labels[q] == 0: labels[q] = cid; stack.append(q)
  typ = ["core" if i in core else "border" if labels[i] else "noise" for i in range(n)]
  return labels, typ
