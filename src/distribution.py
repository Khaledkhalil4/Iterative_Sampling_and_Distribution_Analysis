import numpy as np


def run_simulation(n, M, R):
    """
    Run the iterative sampling simulation with accumulation.

    Process:
      1. Start by sampling M strands from a uniform distribution over n categories.
      2. For each round:
         - Compute the current distribution from the accumulated counts.
         - Sample M strands from this distribution.
         - Add the new counts to the accumulated counts (i.e. duplicate the chosen strands).

    Parameters:
      n (int): Number of strands (categories).
      M (int): Number of strands sampled per round.
      R (int): Number of rounds.

    Returns:
      distributions (list of numpy arrays): List of probability distributions after each round.
      final_counts (numpy array): The final accumulated counts.
    """
    # Start with an initial sample of M strands from a uniform distribution.
    p_uniform = np.ones(n) / n
    counts = np.random.multinomial(M, p_uniform)
    distributions = [counts / np.sum(counts)]

    for _ in range(R):
        total = np.sum(counts)
        current_p = counts / total
        new_counts = np.random.multinomial(M, current_p)
        counts += new_counts  # accumulate the new counts
        distributions.append(counts / np.sum(counts))

    return distributions, counts
