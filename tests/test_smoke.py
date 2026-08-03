"""Hand-checkable smoke tests for every exam tool."""
from exam import *

def test_discrete_kernel():
  # window [2,4] inclusive over {1,2,3,4,5} -> k=3, f = 3/(5*2) = 3/10
  assert abs(discrete_kernel([1, 2, 3, 4, 5], 3, 2) - 3/10) < 1e-12

def test_discrete_kernel_inclusive_boundary():
  # boundary points count: window [1,3] over {1,3} -> k=2
  assert abs(discrete_kernel([1, 3], 2, 2) - 2/(2*2)) < 1e-12

def test_knn_density():
  # data {1,2,4,8}, x=2, k=2, self counts: dists 0,1,2,6 -> r=1, k_adj=2, f=2/(4*2*1)
  assert abs(knn_density([1, 2, 4, 8], 2, 2) - 2/8) < 1e-12

def test_knn_density_ties():
  # x=3 in {1,2,4,5}: dists 1,1,2,2; k=1 -> r=1 but TWO points at d<=1 -> f=2/(4*2)
  assert abs(knn_density([1, 2, 4, 5], 3, 1) - 2/8) < 1e-12

def test_ahc_single_complete():
  D = proxmat([[0], [2], [6]], mand)
  assert [h for *_, h in ahc(D, "single")] == [2, 4]
  assert [h for *_, h in ahc(D, "complete")] == [2, 6]

def test_ahc_ward_matches_scipy():
  import numpy as np
  from scipy.spatial.distance import squareform
  from scipy.cluster.hierarchy import linkage
  pts = [[0, 0], [1, 0], [4, 2], [5, 3], [9, 9]]
  D = proxmat(pts, eucd)
  ours = [h for *_, h in ahc(D, "ward")]
  ref = linkage(squareform(np.array(D), checks=False), "ward")[:, 2]
  assert all(abs(a - b) < 1e-9 for a, b in zip(ours, ref))

def test_match_dendrogram():
  D = proxmat([[0], [2], [6]], mand)
  res = match_dendrogram(D, [2, 6])
  assert res["complete"][1] is True and res["single"][1] is False

def test_lof_symmetric_grid():
  pts = [[0, 0], [0, 1], [1, 0], [1, 1]]
  assert all(abs(x - 1) < 1e-9 for x in lof(pts, 2))

def test_lof_table_matches_lof():
  pts = [[0, 0], [0, 1], [1, 0], [5, 5]]
  _, lofs = lof_table(pts, 2)
  assert all(abs(a - b) < 1e-12 for a, b in zip(lofs, lof(pts, 2)))

def test_analyze_and_check_order():
  res = analyze("A 0 0 / B 0 1 / C 1 0 / D 5 5", metric="euc", k=2, db=(1.5, 3))
  assert res["knn"]["D"] > res["knn"]["A"]
  assert check_order("D,A", res["knn"])
  assert res["dbscan(1.5,3)"]["D"] == (0, "noise")

def test_dbscan_counts_itself():
  labels, types = dbscan([[0], [1], [10]], eps=1.5, minpts=2, d=mand)
  assert types == ["core", "core", "noise"] and labels[2] == 0

def test_apriori_and_rule():
  db = parse_db("A,B,C / A,B / A,C / B,C / A,B,C")
  freqs = apriori(db, 2)
  assert freqs[3] == {("A", "B", "C"): 2}
  sac, rel, conf, lft = rule(db, "A", "B")
  assert (sac, conf) == (3, 3/4) and abs(lft - 15/16) < 1e-12

def test_prunable():
  # {A,B,C} prunable when {B,C} not frequent
  missing = prunable(("A", "B", "C"), [("A", "B"), ("A", "C")])
  assert missing == [{"B", "C"}]
  assert prunable(("A", "B", "C"), [("A", "B"), ("A", "C"), ("B", "C")]) == []

def test_mstep1d():
  mus, vs, prs = mstep1d([1, 2], [[1, 0], [0, 1]])
  assert mus == [1, 2] and vs == [0, 0] and prs == [0.5, 0.5]

def test_mstep1d_weighted():
  # single component, gamma = [1, 1, 1] over [0, 3, 6] -> mu=3, var=6
  mus, vs, prs = mstep1d([0, 3, 6], [1, 1, 1])
  assert mus == [3] and vs == [6] and prs == [1]

def test_param_count():
  assert param_count(3, 1) == 3 + 3 + 2  # k means + k vars + (k-1) priors

def test_simp_silhouette():
  data = [[0], [1], [10], [11]]
  ss = simp_silhouette(data, [0, 0, 1, 1])
  # a = 0.5 for all, b = 9.5 or 10.5 -> s = (b-a)/b
  assert abs(ss[1] - (9.5 - 0.5)/9.5) < 1e-12

def test_mle():
  mu, s2 = mle([1, 2, 3])
  assert mu == 2 and abs(s2 - 2/3) < 1e-12  # /n, not /(n-1)

# ---- merged from tools/ (June 2026 replays) ----

JUNE_Q9 = dict(A=2, B=4, C=10, D=12, E=3, F=20, G=28, H=13, I=25)

def test_kmeans_trace_june_q9():
  clusters, iters = kmeans_trace(JUNE_Q9, [2, 4.5, 6], verbose=False)
  assert iters == 3
  assert clusters == [["A", "B", "E"], ["C", "D", "H"], ["F", "G", "I"]]

def test_analyze_partitions_trap_june_q9():
  parts = {"P1": [["A", "B", "E"], ["C", "D", "H"], ["F", "G", "I"]],
           "P2": [["A", "B", "E"], ["C", "D", "H", "F"], ["G", "I"]]}
  res = analyze_partitions(JUNE_Q9, parts, compare_point="A")
  assert abs(res["P1"][0] - 39 - 1/3) < 1e-9 and res["P1"][1] is True
  assert abs(res["P2"][0] - 63.25) < 1e-9 and res["P2"][1] is True  # the trap

def test_cut_height_june_q4():
  D = [[0, 2, 14, 22, 18], [2, 0, 10, 18, 16], [14, 10, 0, 8, 10],
       [22, 18, 8, 0, 6], [18, 16, 10, 6, 0]]
  cl = cut_height(D, "single", 4, labels=["1", "2", "3", "4", "5"])
  assert cl == [("1", "2"), ("3",), ("4",), ("5",)]  # four clusters, not three

def test_hard_partition():
  assert hard_partition([[0.9, 0.1], [0.3, 0.7]], verbose=False) == [1, 2]

def test_conf_compare_june_q8():
  db = parse_db("A,B,C,D / A,C,D,F / A,C,D,E,G / A,B,D,F / B,C,G / D,F,G / A,B,G / C,D,F,G")
  c1, c2 = conf_compare(db, "AD", "C", moved="D")
  assert c2 <= c1  # conf(A=>CD) <= conf(AD=>C)

def test_dist_compare_june_q3():
  assert dist_compare([[1, 2], [2, 1]]) is False   # Q3.1: Mah != Euc
  assert dist_compare([[1, 0], [0, 1]]) is True    # Sigma = I -> equal

def test_binary_compare_runs():
  binary_compare([1, 1, 0], [1, 0, 1], pad=20)     # smoke: prints, no crash

def test_density_report_june_q1():
  data = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 9, 9, 10, 10, 10, 10, 11]
  r = density_report(data, [("kernel", 4, 1), ("knn", 7, 2), ("knn", 7, 1), ("kernel", 4, 2)])
  assert [abs(a - b) < 1e-12 for a, b in zip(r, [3/20, 7/80, 1/40, 1/5])] == [True]*4
