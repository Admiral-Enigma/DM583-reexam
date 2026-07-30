from typing import Sequence

type Vector = Sequence[float | int]
type Matrix = Sequence[Sequence[float]]

# ---------- numeric distances ----------

def eucd(u: Vector, v: Vector) -> float:
  "Euclidean distance (Minkowski p=2)."
  return sum([(x-y)**2 for x, y in zip(u, v)])**.5

def mand(u: Vector, v: Vector) -> float:
  "Manhattan / city-block distance (Minkowski p=1)."
  return sum([abs(x-y) for x, y in zip(u, v)])

def mink(u: Vector, v: Vector, p: float) -> float:
  "Minkowski distance of order p."
  return sum([abs(x-y)**p for x, y in zip(u, v)])**(1/p)

def supd(u: Vector, v: Vector) -> float:
  "Suprema / Chebyshev distance (Minkowski p -> inf)."
  return max([abs(x-y) for x, y in zip(u, v)])

# ---------- numeric similarities ----------

def innerprod(u: Vector, v: Vector) -> float:
  "Inner (dot) product <u,v>."
  return sum([x*y for x, y in zip(u, v)])

def cosine(u: Vector, v: Vector) -> float:
  "Cosine similarity in [-1,1] (in [0,1] for non-negative data)."
  return innerprod(u, v) / (innerprod(u, u) * innerprod(v, v))**.5

def pearson(u: Vector, v: Vector) -> float:
  "Pearson linear correlation in [-1,1]."
  mu, mv = sum(u)/len(u), sum(v)/len(v)
  du, dv = [x-mu for x in u], [y-mv for y in v]
  return innerprod(du, dv) / (innerprod(du, du)*innerprod(dv, dv))**.5

def ranks(v: Vector) -> list[float]:
  "Ascending ranks (1-based), average rank for ties."
  s = sorted(v)
  return [(s.index(x) + len(s)-1 - s[::-1].index(x))/2 + 1 for x in v]

def spearman(u: Vector, v: Vector) -> float:
  "Spearman rank correlation = Pearson on ranks (robust to outliers)."
  return pearson(ranks(u), ranks(v))

# ---------- binary / categorical ----------

def contingency(u: Vector, v: Vector) -> tuple[int, int, int, int]:
  "Counts (n11, n10, n01, n00) between two binary vectors."
  n11 = sum(1 for x, y in zip(u, v) if x and y)
  n10 = sum(1 for x, y in zip(u, v) if x and not y)
  n01 = sum(1 for x, y in zip(u, v) if not x and y)
  n00 = sum(1 for x, y in zip(u, v) if not x and not y)
  return (n11, n10, n01, n00)

def smc(u: Vector, v: Vector) -> float:
  "Simple Matching Coefficient (symmetric binary): (n11+n00)/n."
  n11, n10, n01, n00 = contingency(u, v)
  return (n11+n00) / (n11+n10+n01+n00)

def jaccard(u: Vector, v: Vector) -> float:
  "Jaccard coefficient (asymmetric binary): n11/(n11+n10+n01)."
  n11, n10, n01, _ = contingency(u, v)
  return n11 / (n11+n10+n01)

# ---------- matrix helpers (Mahalanobis & GMM) ----------

def det(A: Matrix) -> float:
  "Determinant via cofactor expansion."
  n = len(A)
  if n == 1: return A[0][0]
  if n == 2: return A[0][0]*A[1][1] - A[0][1]*A[1][0]
  return sum((-1)**j * A[0][j] * det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(n))

def matinv(A: Matrix) -> Matrix:
  "Matrix inverse via Gauss-Jordan elimination."
  n = len(A)
  M = [list(map(float, A[i])) + [float(i == j) for j in range(n)] for i in range(n)]
  for c in range(n):
    p = max(range(c, n), key=lambda r: abs(M[r][c]))
    M[c], M[p] = M[p], M[c]
    M[c] = [x/M[c][c] for x in M[c]]
    for r in range(n):
      if r != c:
        M[r] = [a - M[r][c]*b for a, b in zip(M[r], M[c])]
  return [row[n:] for row in M]

def covmat(data: Matrix) -> Matrix:
  "Sample covariance matrix (n-1 denominator, like R's cov())."
  n, m = len(data), len(data[0])
  mu = [sum(r[j] for r in data)/n for j in range(m)]
  return [[sum((data[k][i]-mu[i])*(data[k][j]-mu[j]) for k in range(n))/(n-1)
           for j in range(m)] for i in range(m)]

def mahalanobis(x: Vector, mean: Vector, cov: Matrix) -> float:
  "Mahalanobis distance from x to centre 'mean'. Square it for R's mahalanobis() value."
  d, inv = [a-b for a, b in zip(x, mean)], matinv(cov)
  return sum(d[i]*inv[i][j]*d[j] for i in range(len(d)) for j in range(len(d)))**.5

# ---------- pre-processing ----------

def zscore(col: Vector) -> list[float]:
  "z-score standardise: (x-mean)/std (sample std, n-1)."
  m = sum(col)/len(col)
  sd = (sum((x-m)**2 for x in col)/(len(col)-1))**.5
  return [(x-m)/sd for x in col]

def rescale(col: Vector) -> list[float]:
  "Linear rescale to [0,1]: (x-min)/(max-min)."
  lo, hi = min(col), max(col)
  return [(x-lo)/(hi-lo) for x in col]

def ordinal(cats: Sequence[str], order: Sequence[str]) -> list[float]:
  "Encode ordinal values to [0,1]: (rank-1)/(#levels-1)."
  return [order.index(c)/(len(order)-1) for c in cats]

def onehot(cats: Sequence[str], levels: Sequence[str]) -> list[list[int]]:
  "One-hot (1-of-n) encode nominal values."
  return [[1 if c == l else 0 for l in levels] for c in cats]

def dis2sim(d: float, dmax: float | None = None) -> float:
  "Dissimilarity -> similarity. dmax given: 1-d/dmax; else 1/(1+d)."
  return 1 - d/dmax if dmax else 1/(1+d)

def sim2dis(s: float) -> float:
  "Similarity in [0,1] -> dissimilarity: 1-s."
  return 1 - s

def proxmat(data: Matrix, d=eucd) -> Matrix:
  "Pairwise proximity (distance) matrix for rows of data."
  return [[d(a, b) for b in data] for a in data]
