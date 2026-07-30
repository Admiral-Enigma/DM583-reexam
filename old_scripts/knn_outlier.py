import numpy as np
from sklearn.neighbors import NearestNeighbors


def parse_dataset(raw: str) -> list[float]:
    return [float(x.strip()) for x in raw.split(",")]


def knn_outlier_scores(data: list[float], k: int = 1) -> list[float]:
    X = np.array(data).reshape(-1, 1)
    nn = NearestNeighbors(n_neighbors=k + 1, metric="euclidean")
    nn.fit(X)
    distances, _ = nn.kneighbors(X)
    return distances[:, k].tolist()  # column k is the k-th nearest (index 0 is self)


def solve() -> None:
    raw = input("Enter dataset (comma-separated numbers): ")
    data = parse_dataset(raw)
    n = len(data)

    k_raw = input("Enter k [default=1]: ").strip()
    k = int(k_raw) if k_raw else 1

    scores = knn_outlier_scores(data, k)

    sep = "=" * 52
    print(f"\n{sep}")
    print(f"  KNN OUTLIER DETECTION  (k={k})")
    print(sep)
    print(f"Dataset: {data}  (N={n})")
    print()

    # Find nearest neighbour for each point manually for display
    data_arr = np.array(data)
    print(f"{'Point':>8}  {'k-NN':>8}  {'Score (dist)':>12}")
    print("-" * 34)
    for i, xi in enumerate(data):
        dists = np.abs(data_arr - xi)
        dists[i] = np.inf  # exclude self
        idx_nn = np.argpartition(dists, k - 1)[:k]
        nn_pts = sorted(data_arr[idx_nn])
        print(f"{xi:8.2f}  {str(nn_pts):>8}  {scores[i]:12.4f}")
    print()

    print("Note: in 1D, d_p(x,y) = (|x-y|^p)^(1/p) = |x-y| for ALL Minkowski p ≥ 1.")
    print("Therefore the choice of Minkowski distance is irrelevant for 1D data.")
    print()

    claimed_raw = input("Enter claimed outlier scores to compare (comma-separated), or press Enter to skip: ").strip()
    if claimed_raw:
        claimed = [float(x.strip()) for x in claimed_raw.split(",")]
        computed_rounded = [round(s, 6) for s in scores]
        claimed_rounded = [round(c, 6) for c in claimed]
        match = computed_rounded == claimed_rounded

        print()
        print(f"Claimed scores:  {claimed}")
        print(f"Computed scores: {[round(s, 4) for s in scores]}")
        print(f"Match: {'YES' if match else 'NO'}")
        print()
        if match:
            print("VERDICT: TRUE")
            print("  The claimed outlier scores are correct and hold for any Minkowski")
            print("  distance (all reduce to |x-y| in 1D).")
        else:
            print("VERDICT: FALSE")
            print("  The claimed outlier scores do not match the computed values.")
    else:
        print("VERDICT: (no claimed scores provided to compare)")
        print(f"  Computed scores: {[round(s, 4) for s in scores]}")
    print(sep)


if __name__ == "__main__":
    solve()
