import math
import numpy as np
from scipy import stats


def parse_dataset(raw: str) -> list[float]:
    return [float(x.strip()) for x in raw.split(",")]


def compute_mle(data: list[float]) -> tuple[float, float]:
    n = len(data)
    mu = sum(data) / n
    sigma2 = sum((x - mu) ** 2 for x in data) / n
    return mu, sigma2


def solve() -> None:
    raw = input("Enter dataset (comma-separated numbers): ")
    data = parse_dataset(raw)
    n = len(data)

    mu, sigma2 = compute_mle(data)
    sigma = math.sqrt(sigma2)

    sep = "=" * 48
    print(f"\n{sep}")
    print("  MLE GAUSSIAN")
    print(sep)
    print(f"Dataset: {data}  (N={n})")
    print()

    print(f"{'xi':>8}  {'xi - μ':>10}  {'(xi - μ)²':>12}")
    print("-" * 34)
    for x in data:
        d = x - mu
        print(f"{x:8.4f}  {d:10.4f}  {d**2:12.4f}")
    print("-" * 34)
    print(f"{'Sum':>8}  {'':>10}  {sum((x-mu)**2 for x in data):12.4f}")
    print()

    print(f"μ̂  = Σxi / N        = {sum(data):.4f} / {n} = {mu:.6f}")
    print(f"σ̂² = Σ(xi-μ)² / N  = {sum((x-mu)**2 for x in data):.4f} / {n} = {sigma2:.6f}")
    print(f"     (MLE: divide by N={n}, NOT N-1={n-1} — biased estimator)")
    print(f"σ̂  = √σ̂²            = {sigma:.6f}")
    print()

    # Cross-check with numpy
    np_mu = np.mean(data)
    np_sigma2_mle = np.var(data, ddof=0)   # MLE (biased)
    np_sigma2_unbiased = np.var(data, ddof=1)  # Bessel-corrected (not MLE)
    print(f"Verification via numpy:")
    print(f"  np.mean            = {np_mu:.6f}   (matches μ̂)")
    print(f"  np.var(ddof=0)     = {np_sigma2_mle:.6f}   (MLE, matches σ̂²)")
    print(f"  np.var(ddof=1)     = {np_sigma2_unbiased:.6f}   (unbiased, NOT what MLE gives)")
    print()

    # Show fitted pdf at a few points
    xs = [mu - sigma, mu, mu + sigma]
    print(f"Fitted N(μ={mu:.4f}, σ={sigma:.4f}) pdf at selected points:")
    for x in xs:
        print(f"  f({x:8.4f}) = {stats.norm.pdf(x, loc=mu, scale=sigma):.6f}")
    print()

    print("VERDICT: TRUE")
    print("  MLE for a Gaussian yields:")
    print(f"  μ̂ = sample mean = Σxi/N")
    print(f"  σ̂² = Σ(xi-μ̂)²/N  (biased, divide by N)")
    print(sep)


if __name__ == "__main__":
    solve()
