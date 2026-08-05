import sys
from fractions import Fraction
from itertools import combinations

sys.path.insert(0, r"C:\Users\lord-\Desktop\DM583-reexam\src")

from exam.dist import mand, eucd, supd
from exam.outliers import knn_outlier, wknn_outlier, lof, lof_table
from exam.cluster import dbscan

BAR = "=" * 78


def hd(t):
    print("\n" + BAR + "\n" + t + "\n" + BAR)


# ---------------------------------------------------------------- Q2 APRIORI
hd("Q2  Apriori candidate generation (merge step, before pruning)")
L3 = ["ABC", "ABG", "ABH", "ACG", "ADG", "AEH", "AFI", "AGH", "BCG", "BEH",
      "BGH", "CDE", "CDG", "CGH", "DEG", "DEH", "DGH", "EGH"]
L3 = sorted("".join(sorted(s)) for s in L3)

# standard Apriori F_{k-1} x F_{k-1} join: share the first k-2 items (prefix)
prefix_cands = set()
for a, b in combinations(L3, 2):
    if a[:-1] == b[:-1]:
        prefix_cands.add("".join(sorted(set(a) | set(b))))

# loose variant: any two (k-1)-itemsets whose union has size k
loose_cands = set()
for a, b in combinations(L3, 2):
    u = set(a) | set(b)
    if len(u) == 4:
        loose_cands.add("".join(sorted(u)))

print("L3 =", L3)
print("\nPREFIX join (standard Apriori) C4 =", sorted(prefix_cands))
print("LOOSE  join (any 2 shared items) C4 =", sorted(loose_cands))

asked = ["ABCD", "ABDG", "ABCG", "DEGH", "CDGH", "BEGH", "ABGH", "ABCH", "BCGH", "CDEG"]
mine = ["No", "No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No", "Yes"]
print("\n  itemset  prefix  loose   mine")
for it, m in zip(asked, mine):
    print(f"  {it:<8} {'Yes' if it in prefix_cands else 'No':<7} "
          f"{'Yes' if it in loose_cands else 'No':<7} {m}")

# ---------------------------------------------------------------- Q4 EM-GMM
hd("Q4  EM-GMM sub 4: posteriors from densities 0.0086 / 0.0136, priors 0.3 / 0.7")
d1, d2, p1, p2 = 0.0086, 0.0136, 0.3, 0.7
num1, num2 = p1 * d1, p2 * d2
tot = num1 + num2
print(f"  num1 = {p1}*{d1} = {num1:.6g}")
print(f"  num2 = {p2}*{d2} = {num2:.6g}")
print(f"  P(C1|x) = {num1/tot:.6f}   P(C2|x) = {num2/tot:.6f}")
print(f"  claimed 0.213 / 0.787  -> {'MATCHES (True)' if abs(num1/tot-0.213) < 5e-4 else 'does NOT match'}")

# ------------------------------------------------------------ Q5 kmeans eval
hd("Q5  k-Means solution comparison  (A=1 B=2 C=4 D=6 E=8 F=9 G=10)")
Q5 = {"A": 1, "B": 2, "C": 4, "D": 6, "E": 8, "F": 9, "G": 10}
S = {
    "S1": [["A", "B", "C"], ["D", "E", "F", "G"]],
    "S2": [["A", "B"], ["C", "D"], ["E", "F", "G"]],
    "S3": [["A", "B", "C", "D"], ["E", "F", "G"]],
}


def sse_1d(part, data):
    tot = 0.0
    for cl in part:
        c = sum(data[p] for p in cl) / len(cl)
        tot += sum((data[p] - c) ** 2 for p in cl)
    return tot


def simp_sil(part, data, show=False):
    cents = [sum(data[p] for p in cl) / len(cl) for cl in part]
    ss = []
    for i, cl in enumerate(part):
        for p in cl:
            a = abs(data[p] - cents[i])
            b = min(abs(data[p] - cents[j]) for j in range(len(cents)) if j != i)
            s = 0.0 if max(a, b) == 0 else (b - a) / max(a, b)
            ss.append(s)
            if show:
                print(f"    {p}={data[p]:<3} a={a:.4f} b={b:.4f} s={s:.5f}")
    return sum(ss) / len(ss)


res5 = {}
for n, p in S.items():
    cents = [sum(Q5[q] for q in cl) / len(cl) for cl in p]
    print(f"\n{n} = {p}   centroids {[round(c, 4) for c in cents]}")
    sil = simp_sil(p, Q5, show=True)
    res5[n] = (sse_1d(p, Q5), sil)
    print(f"    -> SSE = {res5[n][0]:.5f}   mean simplified silhouette = {sil:.6f}")

print("\nsummary:")
for n, (s, sil) in res5.items():
    print(f"  {n}: SSE={s:.5f}  simpSil={sil:.6f}")
print(f"\n  sub1 'S1 better than S3 (simpSil)' -> {res5['S1'][1] > res5['S3'][1]}")
print(f"  sub2 'S3 better than S1 (SSE)'      -> {res5['S3'][0] < res5['S1'][0]}")
print(f"  sub4 'S2 better than S3 (simpSil)'  -> {res5['S2'][1] > res5['S3'][1]}")
print(f"  sub5 'S1 better than S2 (simpSil)'  -> {res5['S1'][1] > res5['S2'][1]}")

# --------------------------------------------------------------- Q6 OUTLIERS
hd("Q6  Outlier score orderings, Manhattan, k=2, query NOT in own neighbourhood")
lab6 = ["A", "B", "C", "D", "E", "F", "G", "H"]
P6 = [(5, 2), (1, 7), (3, 4), (6, 6), (4, 7), (5, 5), (4, 6), (3, 7)]
k6 = knn_outlier(P6, 2, mand)
w6 = wknn_outlier(P6, 2, mand)
print("  kNN (dist to 2nd NN):  " + "  ".join(f"{l}={v:g}" for l, v in zip(lab6, k6)))
print("  wkNN (avg of 1st,2nd): " + "  ".join(f"{l}={v:g}" for l, v in zip(lab6, w6)))
print("\n  LOF pipeline (k=2, Manhattan):")
_, l6 = lof_table(P6, 2, mand, lab6)
K = dict(zip(lab6, k6)); W = dict(zip(lab6, w6)); L = dict(zip(lab6, l6))


def ordered(seq, sc):
    v = [sc[x] for x in seq]
    ok = all(v[i] >= v[i + 1] - 1e-12 for i in range(len(v) - 1))
    return ok, v


print()
for sub, seq, sc, nm, ans in [
    (1, "ABD", W, "wkNN", "Yes"), (2, "BCD", L, "LOF", "No"),
    (3, "CDE", K, "kNN", "Yes"), (4, "CEG", K, "kNN", "No"),
    (5, "ACD", L, "LOF", "No")]:
    ok, v = ordered(seq, sc)
    print(f"  sub{sub} {','.join(seq)} w.r.t. {nm}: values {[round(x,4) for x in v]}"
          f" -> correctly ordered = {'Yes' if ok else 'No'}   (answered {ans})")

# ----------------------------------------------------------------- Q7 DBSCAN
hd("Q7  DBSCAN, Manhattan, query COUNTS in its own neighbourhood")
lab7 = list("ABCDEFGHIJKLMNOPQRS")
P7 = [(3, 1), (2, 2), (3, 2), (4, 2), (2, 3), (4, 3), (3, 4), (5, 4), (5, 5),
      (6, 5), (7, 5), (8, 5), (3, 6), (6, 6), (7, 6), (2, 7), (6, 7), (7, 7), (5, 8)]
idx = {l: i for i, l in enumerate(lab7)}
eps = 2
nb = {l: sorted(lab7[j] for j in range(len(P7)) if mand(P7[idx[l]], P7[j]) <= eps)
      for l in lab7}
print(f"  eps={eps} Manhattan neighbourhoods (incl. self):")
for l in lab7:
    print(f"    N({l}) = {{{','.join(nb[l])}}}   |N|={len(nb[l])}")

for mp in (2, 3, 4):
    labels, typ = dbscan(P7, eps, mp, mand)
    print(f"\n  --- MinPts={mp}")
    print("    " + "  ".join(f"{l}:{typ[i]}/c{labels[i]}" for i, l in enumerate(lab7)))
    g = {}
    for i, l in enumerate(lab7):
        g.setdefault(labels[i], []).append(l)
    for c in sorted(g):
        print(f"      cluster {c if c else 'NOISE'}: {g[c]}")

print("\n  claims:")
for txt, mp, fn in [
    ("S same cluster as Q (MinPts=3)", 3,
     lambda lb, ty: lb[idx['S']] != 0 and lb[idx['S']] == lb[idx['Q']]),
    ("P directly density reachable from M (MinPts=4)", 4,
     lambda lb, ty: ty[idx['M']] == 'core' and 'P' in nb['M']),
    ("S is noise (MinPts=3)", 3, lambda lb, ty: ty[idx['S']] == 'noise'),
    ("A is core (MinPts=4)", 4, lambda lb, ty: ty[idx['A']] == 'core'),
    ("P same cluster as M (MinPts=2)", 2,
     lambda lb, ty: lb[idx['P']] != 0 and lb[idx['P']] == lb[idx['M']]),
    ("P is border (MinPts=2)", 2, lambda lb, ty: ty[idx['P']] == 'border'),
]:
    lb, ty = dbscan(P7, eps, mp, mand)
    print(f"    {txt:<48} -> {fn(lb, ty)}")

# --------------------------------------------------------------- Q8 1-D kmeans
hd("Q8  1-D k-Means  (A=-2 B=0 C=4 D=8 E=12 F=14 G=16)")
Q8 = {"A": -2, "B": 0, "C": 4, "D": 8, "E": 12, "F": 14, "G": 16}


def stable(part, data):
    cents = [sum(data[p] for p in cl) / len(cl) for cl in part]
    moves = []
    for i, cl in enumerate(part):
        for p in cl:
            best = min(range(len(cents)), key=lambda j: abs(data[p] - cents[j]))
            if abs(data[p] - cents[best]) < abs(data[p] - cents[i]) - 1e-12:
                moves.append(f"{p} -> cluster {best}")
    return not moves, cents, moves


for part in ([["A", "B", "C", "D"], ["E", "F", "G"]],
             [["A", "B", "C"], ["D", "E", "F", "G"]]):
    ok, cents, mv = stable(part, Q8)
    print(f"  {part}: centroids {[round(c,4) for c in cents]}  SSE={sse_1d(part, Q8):.5f}"
          f"  fixed point={ok} {mv}")

print("\n  sub4: init prototypes at F=14 and G=16, one assign+update:")
c = [Q8["F"], Q8["G"]]
asg = {p: min(range(2), key=lambda j: abs(v - c[j])) for p, v in Q8.items()}
cl = [sorted(p for p in Q8 if asg[p] == j) for j in range(2)]
newc = [sum(Q8[p] for p in g) / len(g) for g in cl]
print(f"    assignment {cl} -> new prototypes {newc}")
print(f"    claimed 2.5 and 14 -> {sorted(newc) == [2.5, 14]}")

# ---------------------------------------------------------------- Q9 DENSITY
hd("Q9  Non-parametric density, 2-D, n=8  (same grid as Q6)")
n9 = len(P6)


def discrete2d(q, h, pts=P6, labels=lab6):
    ins = [labels[i] for i, p in enumerate(pts) if supd(p, q) <= h / 2]
    V = h ** 2
    f = Fraction(len(ins), n9 * int(V)) if float(V).is_integer() else None
    print(f"  discrete kernel at {q}, h={h}: window [{q[0]-h/2},{q[0]+h/2}]x"
          f"[{q[1]-h/2},{q[1]+h/2}], V=h^2={V:g}")
    print(f"    inside (k={len(ins)}): {ins}")
    print(f"    f = k/(n*V) = {len(ins)}/({n9}*{V:g}) = {f} = {float(len(ins))/(n9*V):.6g}")
    return f


print("sub1: query = G = (4,6), h=2, claimed 3/32")
f1 = discrete2d((4, 6), 2)
print(f"    -> claim 3/32 is {f1 == Fraction(3,32)}")
print("\nsub3: query = (5,6), h=2, claimed 1/8")
f3 = discrete2d((5, 6), 2)
print(f"    -> claim 1/8 is {f3 == Fraction(1,8)}")

print("\nsub4: kNN density at (5,6), Manhattan, k=2 (tie-adjustable), claimed 1/8")
q = (5, 6)
ds = sorted((mand(P6[i], q), lab6[i]) for i in range(n9))
print("    distances:", ", ".join(f"{l}:{d:g}" for d, l in ds))
r = ds[1][0]
tie = [l for d, l in ds if d <= r]
print(f"    r = 2nd-NN distance = {r:g};  tie-adjusted k = {len(tie)} {tie}")
for vname, V in [("L1 ball (diamond) 2r^2", 2 * r * r), ("square (2r)^2", (2 * r) ** 2)]:
    for kk, klbl in [(len(tie), f"k_adj={len(tie)}"), (2, "k=2 (no tie adj)")]:
        val = Fraction(kk, 1) / Fraction(n9 * V).limit_denominator(10**6)
        print(f"      V={vname:<24} {klbl:<18} f = {val}  ({float(val):.6g})"
              f"{'   <-- equals 1/8' if val == Fraction(1,8) else ''}")

print("\n" + BAR)
print("done")
