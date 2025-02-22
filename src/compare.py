import numpy as np
import matplotlib


matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm
from distribution import run_simulation


def main():
    """
    For each scaling factor c in [3, 10, 25, 50], create a figure with 4 subplots
    corresponding to rounds R in [5, 10, 15, 20]. Each subplot shows:
      - A histogram of the final strand counts (raw counts, i.e. number of strands)
      - An overlay of the fitted normal distribution scaled to the histogram.
    """
    n = 100000  # Number of strands
    scaling_factors = [3, 10, 25, 50]
    round_values = [5, 10, 15, 20]

    for c in scaling_factors:
        # Create a new figure for each scaling factor
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Scaling factor c = {c}", fontsize=16)

        axs = axs.flatten()

        for i, R in enumerate(round_values):
            M = c * n  # Sample size M = c * n
            _, final_counts = run_simulation(n, M, R)

            ax = axs[i]
            num_bins = 100
            # Plot histogram of raw counts (number of strands per bin)
            counts, bins, _ = ax.hist(final_counts, bins=num_bins, alpha=0.6,
                                      color='g', edgecolor='black', density=False)

            # Calculate mean and standard deviation from final_counts
            mu = np.mean(final_counts)
            sigma = np.std(final_counts)

            # Compute bin width from histogram bins
            bin_width = bins[1] - bins[0]
            # Generate x-values spanning the histogram range
            x = np.linspace(bins[0], bins[-1], 100)
            # Calculate the normal PDF and scale it to the histogram counts
            pdf = norm.pdf(x, mu, sigma)
            expected_counts = pdf * n * bin_width
            ax.plot(x, expected_counts, 'k-', lw=2, label='Normal fit')
            ax.legend(fontsize=10)

            ax.set_title(f"Rounds = {R}", fontsize=12)
            ax.set_xlabel("Number of Occurrences", fontsize=10)
            ax.set_ylabel("Number of Strands", fontsize=10)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()


if __name__ == '__main__':
    main()
