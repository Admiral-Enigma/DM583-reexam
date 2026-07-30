from dist import Vector

def innerprod(u: Vector, v: Vector) -> float:
  return sum([x*y for x,y in zip(u, v)])

def posteriors(xs: Vector, priors: Vector) -> Vector:
  """
  Returns posteriors for densities at
  x equal to xs and corresponding priors.
  """
  jprobs = [x*p for x,p in zip(xs, priors)]
  sum_jprobs = sum(jprobs)
  return [p/sum_jprobs for p in jprobs]

def MLE_uni(v: Vector) -> tuple[float, float]:
  """
  Returns (sample mean, sample var)
  """
  k = len(v)
  m = sum(v) / k
  return (m, 1/k * sum([(x - m)**2 for x in v]))


