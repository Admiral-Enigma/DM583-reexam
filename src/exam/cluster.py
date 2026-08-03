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

def _named_1d(data) -> dict[str, float]:
  "Accept {'A': 2, ...} or a plain list (auto-named A, B, C, ...)."
  if isinstance(data, dict):
    return dict(data)
  return {chr(ord("A") + i): v for i, v in enumerate(data)}

def kmeans_trace(data, init, max_iter: int = 50, verbose: bool = True):
  """
  1-D k-Means (Lloyd) with NAMED points and the full trace shown — for the
  'converges in exactly N iterations' subs (June Q9.1).
  data: {'A': 2, 'B': 4, ...} or a list; init: initial centroids.
  One iteration = assign all points, then update centroids. Returns
  (clusters, n_changing_iterations); the run stops when an iteration
  reproduces the previous assignment.
  """
  data = _named_1d(data)
  cents, prev = list(init), None
  if verbose:
    print(f"k-means from centroids {list(init)}:")
  for it in range(1, max_iter + 1):
    assign = {p: min(range(len(cents)), key=lambda j: abs(v - cents[j]))
              for p, v in data.items()}
    clusters = [sorted(p for p in data if assign[p] == j) for j in range(len(cents))]
    cents = [sum(data[p] for p in cl)/len(cl) if cl else cents[j]
             for j, cl in enumerate(clusters)]
    if verbose:
      print(f"  iter {it}: {clusters} -> centroids {[round(c, 4) for c in cents]}")
    if clusters == prev:
      if verbose:
        print(f"  converged: {it - 1} iteration(s) changed the assignment "
              f"(iter {it} confirmed no change).")
      return clusters, it - 1
    prev = clusters
  if verbose: print("  did NOT converge within max_iter")
  return prev, max_iter

def is_fixed_point(data, partition, verbose: bool = True) -> bool:
  """
  Would Lloyd's reassignment step change this 1-D partition? True = k-Means is
  trapped here if it ever arrives (June Q9.2). partition: list of name-lists.
  """
  data = _named_1d(data)
  cents = [sum(data[p] for p in cl)/len(cl) for cl in partition]
  stable = True
  for i, cl in enumerate(partition):
    for p in cl:
      best = min(range(len(cents)), key=lambda j: abs(data[p] - cents[j]))
      if abs(data[p] - cents[best]) < abs(data[p] - cents[i]) - 1e-12:
        stable = False
        if verbose:
          print(f"  {p} would move: |{data[p]:g} - {cents[i]:.4g}| > "
                f"|{data[p]:g} - {cents[best]:.4g}|")
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
      c = sum(data[p] for p in cl)/len(cl)
      s = sum((data[p] - c)**2 for p in cl)
      total += s
      print(f"  {sorted(cl)}: centroid {c:.4g}, SSE {s:.4g}")
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
      cents = [sum(data[p] for p in cl)/len(cl) for cl in part]
      own = next(i for i, cl in enumerate(part) if compare_point in cl)
      a = abs(data[compare_point] - cents[own])
      b = min(abs(data[compare_point] - cents[i]) for i in range(len(cents)) if i != own)
      s = 0.0 if max(a, b) == 0 else (b - a)/max(a, b)
      single = "   (singleton: a=0 -> s=1)" if len(part[own]) == 1 else ""
      print(f"  in {name}: a = {a:.4g}, b = {b:.4g} -> s = {s:.4f}{single}")
  return results

# ---------- agglomerative hierarchical ----------

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
