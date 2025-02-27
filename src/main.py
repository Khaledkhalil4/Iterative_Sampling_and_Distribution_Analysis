import argparse
from distribution import run_simulation
from plotting import plot_counts

def main():
    parser = argparse.ArgumentParser(
        description='Iterative Sampling with Accumulation Simulation'
    )
    parser.add_argument('--num_strands', type=int, default=100000,
                        help='Number of strands (n).')
    parser.add_argument('--scaling_factor', type=int, default=1,
                        help='Scaling factor (c) for M = c * n, must be in range 3 ≤ c ≤ 50')
    parser.add_argument('--rounds', type=int, default=1,
                        help='Number of sampling rounds (R).')
    parser.add_argument('--plot', type=lambda x: (str(x).lower() == 'true'), default=True,
                        help='Whether to generate distribution plots (True/False).')
    args = parser.parse_args()

    n = args.num_strands
    c = args.scaling_factor
    R = args.rounds
    M = c * n  # Sample size per round

    print("Running simulation with accumulation:")
    print("  Number of strands (n):", n)
    print("  Scaling factor (c):", c)
    print("  Sample size per round (M):", M)
    print("  Number of rounds (R):", R)

    distributions, final_counts = run_simulation(n, M, R)

    # Print the count of strands that never received any counts.
    zero_strands = (final_counts == 0).sum()
    print("Number of strands with zero count:", zero_strands)

    if args.plot:
        plot_counts(final_counts)

if __name__ == '__main__':
    main()
