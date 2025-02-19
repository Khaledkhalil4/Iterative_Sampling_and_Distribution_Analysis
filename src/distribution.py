import numpy as np


def run_simulation(n, M, R):
    """
    Run the iterative sampling simulation.

    At each of R rounds:
      - Draw M samples from the current probability distribution over n strands.
      - Update the probability distribution based on the empirical counts.

    Parameters:
      n (int): Number of strands (categories).
      M (int): Sample size per round (M = c * n).
      R (int): Number of rounds.

    Returns:
      distributions (list of numpy arrays): List of probability distributions after each round.
      final_counts (numpy array): The counts from the final round.
    """
    # Start with a uniform distribution
    p = np.ones(n) / n
    distributions = [p.copy()]

    for _ in range(R):
        # Draw a multinomial sample: efficient even for large n
        counts = np.random.multinomial(M, p)
        # Update distribution based on counts
        p = counts / M
        distributions.append(p.copy())

    return distributions, counts


