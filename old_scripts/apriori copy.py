from itertools import combinations as combs

def apriori(db: list[set[str]], max_cat: int, /, thresh: int = 5):
  items: set[str] = set()
  for s in db: items = items.union(s)

  counts: list[dict[frozenset[str], int]] = []
  for i in range(1,max_cat+11):
    count: dict[frozenset[str], int] = {}
    for t in [frozenset(t) for t in combs(items, i)]:
      if i >= 2 and not all(counts[i-2].get(frozenset(x), 0) >= thresh
      for x in combs(t, i-1)):
        continue
      for s in db:
         if t.issubset(s):
           count[t] = count.get(t, 0) + 1
    #print("pre-prune: "+ str(count))
    if not len(count := {k: v for k,v in count.items() if v >= thresh}): break
    counts.append(count)
  print("\n\n".join([str({",".join(k):v for k,v in c.items()}) for c in counts]))

if __name__ == "__main__":
  DB = [ 
    {"A", "B", "C", "D"},
     {"A", "C", "D", "F"},
    {"A", "C", "D", "E", "G"},
    {"A", "B", "D", "F"},
    {"B", "C", "G"},
    {"D", "F", "G"},
    {"A", "B", "G"},
    {"C", "D", "F", "G"},

  ]
  apriori(DB, 3, 3)
