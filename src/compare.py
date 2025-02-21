import numpy as np
import matplotlib

# Use TkAgg or another backend if necessary
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm
from distribution import run_simulation


def main():
    """
    For each scaling factor c in [3, 10, 25, 50], create a separate figure containing a 2x2 grid
    of subplots, each corresponding to a different number of rounds R in [5, 10, 15, 20].
    Each subplot displays:
      - A histogram of the final accumulated counts.
      - An overlay of a fitted normal distribution.
    """
    n = 100000  # Number of strands
    scaling_factors = [3, 10, 25, 50]
    round_values = [5, 10, 15, 20]

    for c in scaling_factors:
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Accumulation with Scaling factor c = {c}", fontsize=16)

        axs = axs.flatten()
        for i, R in enumerate(round_values):
            M = c * n  # Sample size per round
            _, final_counts = run_simulation(n, M, R)

            ax = axs[i]
            num_bins = 100
            counts_hist, bins, _ = ax.hist(final_counts, bins=num_bins, alpha=0.6,
                                           color='g', edgecolor='black', density=False)

            # Fit a normal distribution to final_counts
            mu = np.mean(final_counts)
            sigma = np.std(final_counts)

            bin_width = bins[1] - bins[0]
            x = np.linspace(bins[0], bins[-1], 100)
            pdf = norm.pdf(x, mu, sigma)
            expected_counts = pdf * len(final_counts) * bin_width  # Scale PDF to histogram counts
            ax.plot(x, expected_counts, 'k-', lw=2, label='Normal fit')
            ax.legend(fontsize=10)

            ax.set_title(f"Rounds = {R}", fontsize=12)
            ax.set_xlabel("Accumulated Count")
            ax.set_ylabel("Number of Strands")

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()


if __name__ == '__main__':
    main()
