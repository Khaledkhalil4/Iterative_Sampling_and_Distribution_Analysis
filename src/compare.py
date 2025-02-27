import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm


def run_simulation_intermediate(n, M, R_max):
    """
    Runs one simulation for R_max rounds and returns a list of counts
    at the end of each round. The initial sample is at index 0.
    """
    # Initial sampling from a uniform distribution.
    p_uniform = np.ones(n) / n
    counts = np.random.multinomial(M, p_uniform)
    counts_history = [counts.copy()]

    # Run simulation for R_max rounds, storing counts after each round.
    for r in range(1, R_max + 1):
        current_p = counts / counts.sum()
        new_counts = np.random.multinomial(M, current_p)
        counts += new_counts
        counts_history.append(counts.copy())
    return counts_history


def main():
    """
    For each scaling factor c in [3, 10, 25, 50], run a single simulation (for 20 rounds)
    and create a figure with 4 subplots corresponding to rounds R in [5, 10, 15, 20].
    Each subplot shows:
      - A histogram of the final strand counts (raw counts, i.e. number of strands)
      - An overlay of the fitted normal distribution scaled to the histogram.
      - An annotation with the number of strands that never got any counts.
    """
    n = 100000  # Number of strands
    scaling_factors = [3, 10, 25, 50]
    round_values = [5, 10, 15, 20]
    R_max = max(round_values)

    for c in scaling_factors:
        M = c * n  # Sample size per round

        # Run a single simulation and record intermediate counts.
        counts_history = run_simulation_intermediate(n, M, R_max)

        # Create a new figure for each scaling factor.
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Scaling factor c = {c}", fontsize=16)
        axs = axs.flatten()

        for i, R in enumerate(round_values):
            final_counts = counts_history[R]  # Get counts after R rounds from the same simulation.
            ax = axs[i]
            num_bins = 100

            # Plot histogram of raw counts.
            counts_hist, bins, _ = ax.hist(final_counts, bins=num_bins, alpha=0.6,
                                           color='g', edgecolor='black', density=False)

            # Calculate mean and standard deviation.
            mu = np.mean(final_counts)
            sigma = np.std(final_counts)

            # Compute bin width and generate x-values.
            bin_width = bins[1] - bins[0]
            x = np.linspace(bins[0], bins[-1], 100)
            pdf = norm.pdf(x, mu, sigma)
            expected_counts = pdf * n * bin_width
            ax.plot(x, expected_counts, 'k-', lw=2, label='Normal fit')
            ax.legend(fontsize=10)

            # Annotate with the count of strands that never got any counts.
            zero_strands = (final_counts == 0).sum()
            ax.text(0.05, 0.95, f"Zero strands: {zero_strands}",
                    transform=ax.transAxes, fontsize=10, verticalalignment='top')

            ax.set_title(f"Rounds = {R}", fontsize=12)
            ax.set_xlabel("Number of Occurrences", fontsize=10)
            ax.set_ylabel("Number of Strands", fontsize=10)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()


if __name__ == '__main__':
    main()
