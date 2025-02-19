import numpy as np


def run_simulation(n, M, R):

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


