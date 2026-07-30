from math import log
from dist import Vector

def bayes(likelihood: float, prior: float, evidence: float) -> float:
  "Posterior P(Y|X) = P(X|Y) P(Y) / P(X)."
  return likelihood * prior / evidence

def expect(vals: Vector, probs: Vector) -> float:
  "Expectation E[X] = sum x_i P(x_i)."
  return sum(x*p for x, p in zip(vals, probs))

def mean(v: Vector) -> float:
  "Sample mean."
  return sum(v)/len(v)

def var(v: Vector, sample: bool = True) -> float:
  "Variance. sample=True -> divide by n-1; False -> divide by n (MLE)."
  m = mean(v)
  return sum((x-m)**2 for x in v) / (len(v) - (1 if sample else 0))

def std(v: Vector, sample: bool = True) -> float:
  "Standard deviation (sqrt of var)."
  return var(v, sample)**.5

def cov(u: Vector, v: Vector, sample: bool = True) -> float:
  "Covariance between two equal-length sequences."
  mu, mv = mean(u), mean(v)
  return sum((x-mu)*(y-mv) for x, y in zip(u, v)) / (len(u) - (1 if sample else 0))

def marginal(joint: Vector, axis: int) -> list[float]:
  "Marginal (sum rule) of a 2-D joint table over the given axis (0=rows,1=cols)."
  return [sum(r) for r in joint] if axis == 0 else [sum(c) for c in zip(*joint)]

def entropy(probs: Vector) -> float:
  "Shannon entropy H = -sum p log2 p (ignores zero probabilities)."
  return -sum(p*log(p, 2) for p in probs if p > 0)

def kde(x: float, data: Vector, h: float) -> float:
  "1-D Gaussian kernel density estimate at x with bandwidth h."
  from math import pi, exp
  return sum(exp(-((x-xi)/h)**2/2)/(2*pi)**.5 for xi in data) / (len(data)*h)
