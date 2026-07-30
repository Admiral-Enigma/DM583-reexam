import numpy as np
from sklearn.cluster import DBSCAN


def parse_dataset(raw: str) -> list[float]:
    return [float(x.strip()) for x in raw.split(",")]


def run_dbscan(data: list[float], eps: float, min_samples: int) -> tuple[np.ndarray, dict, list]:
    X = np.array(data).reshape(-1, 1)
    model = DBSCAN(eps=eps, min_samples=min_samples, metric="euclidean")
    labels = model.fit_predict(X)
    cluster_ids = sorted(set(labels) - {-1})
    clusters = {cid: [data[i] for i, l in enumerate(labels) if l == cid] for cid in cluster_ids}
    noise = [data[i] for i, l in enumerate(labels) if l == -1]
    return labels, clusters, noise


def solve() -> None:
    raw = input("Enter dataset (comma-separated numbers): ")
    data = parse_dataset(raw)
    n = len(data)

    eps = float(input("Enter eps (ε): ").strip())
    minpts_raw = input("Enter MinPts values to test (comma-separated): ").strip()
    minpts_list = [int(x.strip()) for x in minpts_raw.split(",")]

    sep = "=" * 56
    print(f"\n{sep}")
    print(f"  DBSCAN  (ε={eps})")
    print(sep)
    print(f"Dataset: {data}  (N={n})")
    print()
    print("Note: sklearn DBSCAN counts a point itself toward min_samples.")
    print(f"  min_samples=M means: ≥M points within ε (including the point).")
    print(f"  So min_samples=1 → every point is always a core point.")
    print(f"  And min_samples=2 → a point needs ≥1 OTHER point within ε.")
    print()

    # Show neighbourhood sizes for each point
    data_arr = np.array(data)
    print(f"Neighbourhood sizes |N_ε(xi)| (including xi itself):")
    print(f"{'Point':>8}  {'|N_ε|':>6}  Neighbours within ε={eps}")
    print("-" * 48)
    for xi in data:
        nbrs = [xj for xj in data if abs(xj - xi) <= eps]
        print(f"{xi:8.2f}  {len(nbrs):6d}  {nbrs}")
    print()

    results = {}
    for mp in minpts_list:
        labels, clusters, noise = run_dbscan(data, eps, mp)
        results[mp] = (labels, clusters, noise)

        print(f"--- MinPts = {mp} ---")
        for cid, members in clusters.items():
            print(f"  Cluster {cid+1}: {members}")
        if noise:
            print(f"  NOISE:     {noise}")
        print(f"  → {len(clusters)} cluster(s), {len(noise)} noise point(s)")
        print()

    # Verdict: compare cluster counts
    counts = {mp: len(results[mp][1]) for mp in minpts_list}
    all_same = len(set(counts.values())) == 1
    first_count = counts[minpts_list[0]]

    claimed_raw = input(
        "Enter the claimed number of clusters for all MinPts values (e.g. '4'), or press Enter to skip: "
    ).strip()

    print()
    if claimed_raw:
        claimed_n = int(claimed_raw)
        if all_same and first_count == claimed_n:
            print("VERDICT: TRUE")
            print(f"  All tested MinPts values produce {claimed_n} cluster(s) as claimed.")
        else:
            print("VERDICT: FALSE")
            details = ", ".join(f"MinPts={mp}→{counts[mp]} cluster(s)" for mp in minpts_list)
            print(f"  Cluster counts: {details}")
            if not all_same:
                print("  The MinPts values produce different numbers of clusters.")
            if any(counts[mp] != claimed_n for mp in minpts_list):
                print(f"  At least one result does not match the claimed {claimed_n} cluster(s).")
    else:
        details = ", ".join(f"MinPts={mp}→{counts[mp]} cluster(s)" for mp in minpts_list)
        print(f"VERDICT: Cluster counts are: {details}")
    print(sep)


if __name__ == "__main__":
    solve()
