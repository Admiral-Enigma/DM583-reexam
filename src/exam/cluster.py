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
