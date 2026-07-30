from dist import Vector, Matrix, eucd

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

# ---------- agglomerative hierarchical ----------

def ahc(D: Matrix, method: str = "single") -> list[tuple]:
  """
  Agglomerative hierarchical clustering from distance matrix D.
  method in {single, complete, average, ward}.
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
        dnew = ((len(a)+len(c))*da + (len(b)+len(c))*db - len(c)*dist[key(a, b)])/s
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
