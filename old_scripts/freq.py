from itertools import combinations as combs

type DB = list[set[str]]

def items(db: DB) -> set[str]:
  "All distinct items in the database."
  return set().union(*db)

def support(db: DB, itemset) -> int:
  "Support COUNT of an itemset = number of transactions containing all its items."
  s = set(itemset)
  return sum(1 for t in db if s <= t)

def confidence(db: DB, ante, cons) -> float:
  "Confidence of rule ante => cons = supp(ante U cons) / supp(ante)."
  return support(db, set(ante) | set(cons)) / support(db, ante)

def lift(db: DB, ante, cons) -> float:
  "Lift = conf(ante=>cons) / f(cons). >1 positive assoc, =1 independent, <1 negative."
  return confidence(db, ante, cons) / (support(db, cons)/len(db))

def conviction(db: DB, ante, cons) -> float:
  "Conviction = (1 - f(cons)) / (1 - conf(ante=>cons)). inf if confidence = 1."
  c = confidence(db, ante, cons)
  return float("inf") if c == 1 else (1 - support(db, cons)/len(db)) / (1 - c)

def rule_jaccard(db: DB, ante, cons) -> float:
  "Jaccard of a rule = supp(AUB)/(supp(A)+supp(B)-supp(AUB))."
  a, b, ab = support(db, ante), support(db, cons), support(db, set(ante) | set(cons))
  return ab / (a + b - ab)

def is_closed(db: DB, itemset) -> bool:
  "Closed = frequent itemset with NO superset of the SAME support."
  s0 = support(db, itemset)
  return all(support(db, set(itemset) | {x}) < s0 for x in items(db) - set(itemset))

def is_maximal(db: DB, itemset, thresh: int = 5) -> bool:
  "Maximal = frequent itemset with NO frequent superset (support >= thresh)."
  return all(support(db, set(itemset) | {x}) < thresh for x in items(db) - set(itemset))

def rules(db: DB, itemset, min_conf: float = 0.0) -> list[tuple]:
  """
  All association rules from one (frequent) itemset.
  Returns [(antecedent, consequent, support, confidence), ...] with conf >= min_conf.
  """
  it, out = list(itemset), []
  for r in range(1, len(it)):
    for cons in combs(it, r):
      ante = set(it) - set(cons)
      c = confidence(db, ante, cons)
      if c >= min_conf:
        out.append((ante, set(cons), support(db, itemset), c))
  return out
