from fractions import Fraction
from itertools import combinations as combs

type DB = list[set[str]]

def parse_db(text: str) -> DB:
  """
  Parse a transaction DB pasted as 'A,B,C / B,D / ...' (or one transaction per
  line; optional 'id:' prefixes are stripped). Items uppercased.
  """
  rows = [r for r in text.replace("/", "\n").splitlines() if r.strip()]
  return [{x.strip().upper() for x in r.split(":", 1)[-1].replace(",", " ").split() if x.strip()}
          for r in rows]

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

def rule(db: DB, ante, cons, verbose: bool = True) -> tuple[int, float, float, float]:
  """
  One-liner rule report for ante => cons: support count, relative support,
  confidence (as a fraction) and lift, all with the numbers behind them.
  ante/cons: iterables of items ('AB' means items 'A','B').
  Returns (supp_count, rel_supp, confidence, lift).
  """
  A, C = set(ante), set(cons)
  n = len(db)
  sac, sa, sc = support(db, A | C), support(db, A), support(db, C)
  rel, conf = Fraction(sac, n), Fraction(sac, sa)
  lft = conf / Fraction(sc, n)
  if verbose:
    print(f"rule {sorted(A)} => {sorted(C)}   n={n}")
    print(f"  supp count s(A u C) = {sac}   s(A) = {sa}   s(C) = {sc}")
    print(f"  rel support = {sac}/{n} = {rel} = {float(rel):.4f}")
    print(f"  confidence  = s(AuC)/s(A) = {sac}/{sa} = {conf} = {float(conf):.4f}")
    print(f"  lift        = conf/(s(C)/n) = ({conf})/({sc}/{n}) = {lft} = {float(lft):.4f}")
  return sac, float(rel), float(conf), float(lft)

def prunable(candidate, frequent_prev, verbose: bool = True) -> list[set]:
  """
  Apriori prune check for one k-candidate: which of its (k-1)-subsets are
  missing from frequent_prev (iterable of frequent (k-1)-itemsets)?
  Non-empty result => candidate is pruned. Prints every subset's status.
  """
  freq = {frozenset(f) for f in frequent_prev}
  cand = sorted(set(candidate))
  missing = []
  for s in combs(cand, len(cand)-1):
    ok = frozenset(s) in freq
    if not ok: missing.append(set(s))
    if verbose: print(f"  subset {set(s)}: {'frequent' if ok else 'NOT frequent -> prune'}")
  if verbose:
    print(f"  => {set(cand)} is {'PRUNED' if missing else 'kept (all subsets frequent)'}")
  return missing

def conf_compare(db: DB, ante, cons, moved) -> tuple[Fraction, Fraction]:
  """
  Confidence monotonicity check (June Q8.1): moving items `moved` from the
  antecedent to the consequent can only LOWER (or keep) the confidence:
  conf(A\\M => C u M) <= conf(A => C). Prints both as fractions.
  """
  A, C, M = set(ante), set(cons), set(moved)
  c1 = Fraction(support(db, A | C), support(db, A))
  A2, C2 = A - M, C | M
  c2 = Fraction(support(db, A2 | C2), support(db, A2))
  rel = "<=" if c2 <= c1 else "> (!!)"
  print(f"  conf({sorted(A)}=>{sorted(C)}) = {c1} = {float(c1):.4f}")
  print(f"  conf({sorted(A2)}=>{sorted(C2)}) = {c2} = {float(c2):.4f}   {rel}")
  return c1, c2

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
