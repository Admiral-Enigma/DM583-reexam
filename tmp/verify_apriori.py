import sys
sys.path.insert(0, r"C:\Users\lord-\Desktop\DM583-reexam\src")
from exam.freq import parse_db, support
from exam.apriori import apriori, generate_join

TXT = """A B C / A B C D G / A B C G H / A B E F G H I / A B E F H I /
A C D F G I / A D E G H / B C D E G H / C D E / C D E G H"""
db = parse_db(TXT)
print("N =", len(db))
for i, t in enumerate(db, 1):
    print(f"  {i}: {''.join(sorted(t))}")

allf = apriori(db, 3)

got_L3 = sorted("".join(t) for t in allf.get(3, {}))
exam_L3 = sorted(["ABC", "ABG", "ABH", "ACG", "ADG", "AEH", "AFI", "AGH", "BCG",
                  "BEH", "BGH", "CDE", "CDG", "CGH", "DEG", "DEH", "DGH", "EGH"])
print("\ncomputed L3:", got_L3)
print("exam's   L3:", exam_L3)
print("MATCH:", got_L3 == exam_L3)

prev = sorted(allf[3])
C4 = generate_join(prev)
print("\nC4 from toolkit generate_join (prefix rule):",
      sorted("".join(c) for c in C4))
