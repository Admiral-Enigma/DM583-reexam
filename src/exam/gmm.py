from math import pi, exp
from .dist import Vector, Matrix, det, matinv

def gauss(x: float, mu: float, var: float) -> float:
  "1-D Normal pdf N(x | mu, var). 'var' is the variance (sigma squared)."
  return exp(-(x-mu)**2 / (2*var)) / (2*pi*var)**.5

def mvgauss(x: Vector, mean: Vector, cov: Matrix) -> float:
  "Multivariate Normal pdf N(x | mean, cov)."
  k = len(x)
  dv, inv = [a-b for a, b in zip(x, mean)], matinv(cov)
  q = sum(dv[i]*inv[i][j]*dv[j] for i in range(k) for j in range(k))
  return exp(-q/2) / ((2*pi)**(k/2) * det(cov)**.5)

def responsibilities(densities: Vector, priors: Vector) -> list[float]:
  """
  E-step posteriors (responsibilities) gamma_i for ONE point, given each
  component's density at that point and the priors pi_i. Uses Bayes' rule.
  Hard partition = argmax over these posteriors.
  """
  joint = [d*p for d, p in zip(densities, priors)]
  return [j/sum(joint) for j in joint]

def estep(data: Matrix, means: Matrix, covs: list[Matrix], priors: Vector) -> Matrix:
  "Full E-step: responsibility matrix gamma[j][i] for point j, component i."
  return [responsibilities([mvgauss(x, means[i], covs[i]) for i in range(len(priors))], priors)
          for x in data]

def mstep(data: Matrix, gamma: Matrix) -> tuple[Matrix, list[Matrix], list[float]]:
  "Full multivariate M-step: update (means, covs, priors) from responsibilities gamma."
  n, k, m = len(data), len(gamma[0]), len(data[0])
  Ni = [sum(gamma[j][i] for j in range(n)) for i in range(k)]
  means = [[sum(gamma[j][i]*data[j][d] for j in range(n))/Ni[i] for d in range(m)] for i in range(k)]
  covs = [[[sum(gamma[j][i]*(data[j][a]-means[i][a])*(data[j][b]-means[i][b])
                for j in range(n))/Ni[i] for b in range(m)] for a in range(m)] for i in range(k)]
  return means, covs, [Ni[i]/n for i in range(k)]

def mstep1d(xs: Vector, gamma, verbose: bool = True) -> tuple[list, list, list]:
  """
  1-D M-step with the work shown: per component prints Sum(gamma), prior =
  Sum(gamma)/n, mu = Sum(gamma*x)/Sum(gamma), var = Sum(gamma*(x-mu)^2)/Sum(gamma),
  each with the explicit numerator/denominator (exam distractors swap them).
  gamma[j][i] = responsibility of point j for component i (a flat list works
  for one component). Returns (mus, vars, priors).
  """
  if gamma and not isinstance(gamma[0], (list, tuple)):
    gamma = [[g] for g in gamma]
  n, k = len(xs), len(gamma[0])
  mus, vs, prs = [], [], []
  for i in range(k):
    g = [gamma[j][i] for j in range(n)]
    Ni = sum(g)
    num_mu = sum(gj*x for gj, x in zip(g, xs))
    mu = num_mu/Ni
    num_v = sum(gj*(x-mu)**2 for gj, x in zip(g, xs))
    v = num_v/Ni
    mus.append(mu); vs.append(v); prs.append(Ni/n)
    if verbose:
      print(f"component {i+1}:")
      print(f"  Sum(g)  = {Ni:.6g}")
      print(f"  prior   = Sum(g)/n           = {Ni:.6g}/{n} = {Ni/n:.6g}")
      print(f"  mu      = Sum(g*x)/Sum(g)    = {num_mu:.6g}/{Ni:.6g} = {mu:.6g}")
      print(f"  var     = Sum(g*(x-mu)^2)/Sum(g) = {num_v:.6g}/{Ni:.6g} = {v:.6g}")
  return mus, vs, prs

def hard_partition(gamma: Matrix, labels=None, verbose: bool = True) -> list[int]:
  """
  MAP hard partition from posteriors alone: point j -> argmax_i gamma[j][i]
  (1-based component ids). The exam point: the posteriors SUFFICE — no other
  quantities needed (June Q7.3).
  """
  out = [max(range(len(row)), key=lambda i: row[i]) + 1 for row in gamma]
  if verbose:
    print("hard partition (argmax posterior — posteriors alone suffice):")
    for j, (row, c) in enumerate(zip(gamma, out)):
      name = labels[j] if labels else f"x{j+1}"
      print(f"  {name}: gammas {list(row)} -> C{c}")
  return out

def check_claim(name: str, computed: float, claimed: float, tol: float = 1e-4) -> bool:
  "Compare a computed quantity against an exam statement's claimed value."
  ok = abs(float(computed) - float(claimed)) < tol
  print(f"  claim '{name}': claimed {float(claimed):.4f}, "
        f"computed {float(computed):.4f} -> {'TRUE' if ok else 'FALSE'}")
  return ok

def param_count(k: int, d: int = 1, cov: str = "full") -> int:
  """
  Number of free parameters of a d-dim GMM with k components; prints the
  breakdown (1-D: k means + k variances + (k-1) priors).
  cov in {full, diag, spherical}.
  """
  means = k*d
  covs = {"full": k*d*(d+1)//2, "diag": k*d, "spherical": k}[cov]
  priors = k - 1
  print(f"means:     k*d = {k}*{d} = {means}")
  if d == 1:
    print(f"variances: k = {covs}")
  else:
    print(f"cov ({cov}): {covs}   (full: k*d(d+1)/2, diag: k*d, spherical: k)")
  print(f"priors:    k-1 = {priors}   (they sum to 1)")
  total = means + covs + priors
  print(f"total = {means} + {covs} + {priors} = {total}")
  return total
