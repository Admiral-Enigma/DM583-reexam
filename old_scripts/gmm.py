from math import pi, exp
from dist import Vector, Matrix, det, matinv

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
  (Same as misc.posteriors; here named for the GMM context.)
  """
  joint = [d*p for d, p in zip(densities, priors)]
  return [j/sum(joint) for j in joint]

def estep(data: Matrix, means: Matrix, covs: list[Matrix], priors: Vector) -> Matrix:
  "Full E-step: responsibility matrix gamma[j][i] for point j, component i."
  return [responsibilities([mvgauss(x, means[i], covs[i]) for i in range(len(priors))], priors)
          for x in data]

def mstep(data: Matrix, gamma: Matrix) -> tuple[Matrix, list[Matrix], list[float]]:
  "Full M-step: update (means, covs, priors) from responsibility matrix gamma."
  n, k, m = len(data), len(gamma[0]), len(data[0])
  Ni = [sum(gamma[j][i] for j in range(n)) for i in range(k)]
  means = [[sum(gamma[j][i]*data[j][d] for j in range(n))/Ni[i] for d in range(m)] for i in range(k)]
  covs = [[[sum(gamma[j][i]*(data[j][a]-means[i][a])*(data[j][b]-means[i][b])
                for j in range(n))/Ni[i] for b in range(m)] for a in range(m)] for i in range(k)]
  return means, covs, [Ni[i]/n for i in range(k)]
