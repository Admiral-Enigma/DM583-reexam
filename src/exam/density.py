from fractions import Fraction
from .dist import Vector

def _frac(k: int, n: int, v: float) -> Fraction:
  "Exact fraction k/(n*v); v may be a float like 0.5."
  return Fraction(k, n) / Fraction(v).limit_denominator(10**6)

def discrete_kernel(data: Vector, x: float, h: float, verbose: bool = True) -> float:
  """
  Discrete (box/uniform) kernel density estimate at x.
  Fix the volume: window [x-h/2, x+h/2] INCLUSIVE, count k points inside,
  f(x) = k/(n*h). Prints window, points inside and the fraction in lowest terms.
  """
  n = len(data)
  lo, hi = x - h/2, x + h/2
  inside = sorted(xi for xi in data if lo <= xi <= hi)
  k = len(inside)
  f = _frac(k, n, h)
  if verbose:
    print(f"window = [{lo:g}, {hi:g}] (inclusive), h={h:g}, n={n}")
    print(f"points inside (k={k}): {inside}")
    print(f"f({x:g}) = k/(n*h) = {k}/({n}*{h:g}) = {f} = {float(f):.6g}")
  return float(f)

def density_report(data: Vector, queries: list[tuple]) -> list[float]:
  """
  One shot for a June-Q1-style question. queries: list of
  ('kernel', x, h) / ('knn', x, k) tuples, evaluated in order with full work.
  """
  print(f"data (n={len(data)}): {sorted(data)}\n")
  out = []
  for kind, x, p in queries:
    out.append(discrete_kernel(data, x, p) if kind == "kernel"
               else knn_density(data, x, p))
    print()
  return out

def knn_density(data: Vector, x: float, k: int,
                include_self: bool = True, verbose: bool = True) -> float:
  """
  1-D kNN density estimate at x.
  Fix k: r = distance to the k-th NN, tie-adjust k to ALL points with d <= r,
  V = 2r, f(x) = k_adj/(n*2r). include_self: if x is a data point it counts
  itself (the plain f = k/(nV) convention); set False to exclude it.
  Prints r, the tie-adjusted count and the fraction in lowest terms.
  """
  n = len(data)
  pairs = sorted((abs(xi - x), xi) for xi in data)
  if not include_self and pairs and pairs[0][0] == 0:
    pairs = pairs[1:]
  r = pairs[k-1][0]
  inside = [xi for d, xi in pairs if d <= r]
  k_adj = len(inside)
  if verbose:
    print(f"distances to x={x:g} (ascending): " + ", ".join(f"{xi:g}:{d:g}" for d, xi in pairs))
    print(f"r = d(k-th NN, k={k}) = {r:g}   V = 2r = {2*r:g}")
    print(f"tie-adjusted k = #points with d <= r = {k_adj}: {sorted(inside)}")
  if r == 0:
    if verbose: print(f"f({x:g}) = infinite (r = 0, duplicate points at x)")
    return float("inf")
  f = _frac(k_adj, n, 2*r)
  if verbose:
    print(f"f({x:g}) = k/(n*2r) = {k_adj}/({n}*{2*r:g}) = {f} = {float(f):.6g}")
  return float(f)
