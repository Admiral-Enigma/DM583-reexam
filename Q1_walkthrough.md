# Q1 walkthrough — Non-parametric density estimation (12 pts)

A complete re-solve of June's worst question (−6.0) using the new tools, exactly as it
should go on exam day. Everything below is real, unedited tool output.

## The question

Data (n = 20):

```
{1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 9, 9, 10, 10, 10, 10, 11}
```

Formula family `f(x) = k / (n·V)`, two directions:

- **Discrete (box) kernel** — *fix the volume, count the points*: window
  `[x − h/2, x + h/2]` (boundaries **inclusive**), V = h, k = #points in the window.
- **kNN density** — *fix the count, find the volume*: r = distance to the k-th NN,
  **tie-adjust** k to *all* points with d ≤ r, V = 2r (1-D ball).

Four True/False claims, ±3 each:

| Sub | Claim |
|-----|-------|
| 1 | Discrete kernel, x=4, h=1 → f = 1/10 |
| 2 | kNN density, x=7, k=2 (tie-adjusted) → f = 3/80 |
| 3 | kNN density, x=7, k=1 → f = 1/40 |
| 4 | Discrete kernel, x=4, h=2 → f = 1/5 |

## Exam-day workflow

```
uv run python
>>> from exam import *
>>> data = [1,1,2,2,3,4,4,4,5,5,5,5,6,9,9,10,10,10,10,11]   # ~30s to type, count n!
>>> len(data)
20
```

Typing the dataset and immediately checking `len(data) == 20` is the whole data-entry
step. Then one call per sub.

---

## Sub 1 — kernel, x=4, h=1: claim f = 1/10

```
>>> discrete_kernel(data, 4, 1)
window = [3.5, 4.5] (inclusive), h=1, n=20
points inside (k=3): [4, 4, 4]
f(4) = k/(n*h) = 3/(20*1) = 3/20 = 0.15
```

By hand: window `[4 − 0.5, 4 + 0.5] = [3.5, 4.5]`. The only values in range are the
three 4s → k = 3. So f = 3/(20·1) = **3/20 ≠ 1/10**.

The distractor 1/10 = 2/20 is what you get by miscounting the duplicate 4s (the data
has *three* 4s — duplicates count individually).

**Answer: FALSE** ✓ (+3 — this one was also right in June)

## Sub 2 — kNN, x=7, k=2, tie-adjusted: claim f = 3/80

```
>>> knn_density(data, 7, 2)
distances to x=7 (ascending): 6:1, 5:2, 5:2, 5:2, 5:2, 9:2, 9:2, 4:3, 4:3, 4:3, 10:3, ...
r = d(k-th NN, k=2) = 2   V = 2r = 4
tie-adjusted k = #points with d <= r = 7: [5, 5, 5, 5, 6, 9, 9]
f(7) = k/(n*2r) = 7/(20*4) = 7/80 = 0.0875
```

By hand: nearest neighbour of 7 is 6 (d=1). The 2nd-NN distance is r = 2 — but **six**
points sit at exactly d = 2 (the four 5s and the two 9s). Tie adjustment counts them
all: k = 1 + 6 = 7 points in the ball [5, 9]. V = 2r = 4.
So f = 7/(20·4) = **7/80 ≠ 3/80**.

The distractor 3/80 uses k = 3 (i.e. "the 6, one 5, one 9" — counting *values* instead
of *points*, no tie adjustment). This is exactly the trap that cost −3 in June: the
claim was marked True.

**Answer: FALSE** (was ✗ in June, −3)

## Sub 3 — kNN, x=7, k=1: claim f = 1/40

```
>>> knn_density(data, 7, 1)
r = d(k-th NN, k=1) = 1   V = 2r = 2
tie-adjusted k = #points with d <= r = 1: [6]
f(7) = k/(n*2r) = 1/(20*2) = 1/40 = 0.025
```

By hand: 1st NN is the single point 6 at r = 1. No other point at d ≤ 1, so no tie
adjustment: k = 1, V = 2·1 = 2. f = 1/(20·2) = **1/40 exactly**.

June answered False — probably distrust of the previous sub bleeding over. The claim
is a clean exact match.

**Answer: TRUE** (was ✗ in June, −3)

## Sub 4 — kernel, x=4, h=2: claim f = 1/5

```
>>> discrete_kernel(data, 4, 2)
window = [3, 5] (inclusive), h=2, n=20
points inside (k=8): [3, 4, 4, 4, 5, 5, 5, 5]
f(4) = k/(n*h) = 8/(20*2) = 1/5 = 0.2
```

By hand: window `[4 − 1, 4 + 1] = [3, 5]`, boundaries **inclusive** — that's the trap.
Inside: the 3, three 4s, and all four 5s (5 is *on* the boundary and counts) → k = 8.
f = 8/(20·2) = 8/40 = **1/5 exactly**.

Excluding the boundary points (the 3 and the four 5s) gives 3/40 — call it False — which
is what happened in June (−3).

**Answer: TRUE** (was ✗ in June, −3)

---

## Result

| Sub | Claim | Computed | Verdict | June | Now |
|-----|-------|----------|---------|------|-----|
| 1 | kernel x=4, h=1 → 1/10 | 3/20 | **False** | ✓ +3 | ✓ +3 |
| 2 | kNN x=7, k=2 → 3/80 | 7/80 | **False** | ✗ −3 | ✓ +3 |
| 3 | kNN x=7, k=1 → 1/40 | 1/40 | **True** | ✗ −3 | ✓ +3 |
| 4 | kernel x=4, h=2 → 1/5 | 1/5 | **True** | ✗ −3 | ✓ +3 |

**−6.0 → +12.0.** Every sub is answered from a computed value, none from recall, so
nothing needs to be blanked.

## The three traps this question packs (all hit in June)

1. **Duplicates count individually** — the data is a multiset; three 4s are three points.
2. **Window boundaries are inclusive** — h=2 at x=4 means [3, 5] *including* 3 and 5.
3. **Tie adjustment goes up, not down** — if several points sit exactly at the k-NN
   radius, k grows to include *all* of them; V stays 2r.

And the meta-rule from `PLAN.md` §0: each claimed fraction is either an *exact* match
of the computed value or it's wrong — never accept "close". `discrete_kernel` /
`knn_density` print the fraction in lowest terms precisely so the comparison is
exact-or-nothing.
