from .dist import Vector, Matrix, eucd

def db_outlier(data: Matrix, eps: float, pi: float, d=eucd) -> list[bool]:
  """
  DB(eps, pi)-outliers (Knorr & Ng). True if at most fraction pi of the
  OTHER points lie within distance eps of the point.
  """
  n = len(data)
  return [sum(1 for j in range(n) if j != i and d(data[i], data[j]) <= eps)/(n-1) <= pi
          for i in range(n)]

def _sorted_dists(data: Matrix, i: int, d) -> list[float]:
  "Distances from point i to all OTHER points, ascending."
  return sorted(d(data[i], data[j]) for j in range(len(data)) if j != i)

def knn_outlier(data: Matrix, k: int, d=eucd) -> list[float]:
  "kNN outlier score: distance to the k-th nearest neighbour."
  return [_sorted_dists(data, i, d)[k-1] for i in range(len(data))]

def wknn_outlier(data: Matrix, k: int, d=eucd) -> list[float]:
  "Weighted kNN outlier score: average distance to the 1st..k-th NN."
  return [sum(_sorted_dists(data, i, d)[:k])/k for i in range(len(data))]

def kdist(data: Matrix, i: int, k: int, d=eucd) -> float:
  "k-distance of point i (distance to its k-th nearest neighbour)."
  return _sorted_dists(data, i, d)[k-1]

def knn(data: Matrix, i: int, k: int, d=eucd) -> list[int]:
  "Indices of the k-nearest neighbours of i (ties at k-distance included)."
  kd = kdist(data, i, k, d)
  return [j for j in range(len(data)) if j != i and d(data[i], data[j]) <= kd]

def reachdist(data: Matrix, p: int, o: int, k: int, d=eucd) -> float:
  "Reachability distance reach_dist_k(p, o) = max(k-distance(o), d(p,o))."
  return max(kdist(data, o, k, d), d(data[p], data[o]))

def lrd(data: Matrix, i: int, k: int, d=eucd) -> float:
  "Local reachability density of i = 1 / mean reach_dist to its kNN."
  N = knn(data, i, k, d)
  return 1 / (sum(reachdist(data, i, o, k, d) for o in N)/len(N))

def lof(data: Matrix, k: int, d=eucd) -> list[float]:
  """
  Local Outlier Factor for every point. LOF ~ 1 inlier; LOF >> 1 outlier.
  LOF(i) = mean( lrd(o)/lrd(i) ) over o in kNN(i).
  """
  return [sum(lrd(data, o, k, d) for o in knn(data, i, k, d))
          / (len(knn(data, i, k, d)) * lrd(data, i, k, d)) for i in range(len(data))]

def lof_table(data: Matrix, k: int, d=eucd, labels=None) -> tuple[list[float], list[float]]:
  """
  Print the full LOF pipeline per point: k-dist, kNN neighbourhood (ties included),
  each reach-dist = max(k-dist(o), d(p,o)), lrd, LOF. Returns (lrds, lofs).
  """
  n = len(data)
  name = (lambda i: labels[i]) if labels else (lambda i: str(i))
  Ns = [knn(data, i, k, d) for i in range(n)]
  lrds = [lrd(data, i, k, d) for i in range(n)]
  lofs = []
  for i in range(n):
    rds = [f"rd({name(i)}<-{name(o)})=max({kdist(data,o,k,d):g},{d(data[i],data[o]):g})={reachdist(data,i,o,k,d):g}"
           for o in Ns[i]]
    L = sum(lrds[o] for o in Ns[i]) / (len(Ns[i]) * lrds[i])
    lofs.append(L)
    print(f"  {name(i)}: k-dist={kdist(data,i,k,d):g}  N_{k}={{{','.join(name(o) for o in Ns[i])}}}"
          f"  lrd={lrds[i]:.4f}  LOF={L:.4f}")
    print(f"      {'  '.join(rds)}")
  return lrds, lofs
