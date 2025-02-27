import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def plot_counts(counts, bins=100, show=True, filename=None):
    """
    Plot a histogram of the final accumulated counts with an overlay of a fitted normal curve.

    Parameters:
      counts (numpy array): Accumulated counts for each strand.
      bins (int): Number of bins for the histogram.
      show (bool): If True, display the plot.
      filename (str): If provided, save the plot to this file.
    """
    plt.figure(figsize=(10, 6))
    # Plot histogram (raw counts)
    counts_hist, bin_edges, _ = plt.hist(counts, bins=bins, edgecolor='black',
                                         color='g', alpha=0.6, density=False)

    # Compute mean and standard deviation from the accumulated counts
    mu = np.mean(counts)
    sigma = np.std(counts)

    # Compute bin width for scaling the normal curve
    bin_width = bin_edges[1] - bin_edges[0]
    x = np.linspace(bin_edges[0], bin_edges[-1], 100)
    pdf = norm.pdf(x, mu, sigma)
    # Scale PDF to expected counts: (total number of strands) * (bin width) * PDF
    expected_counts = pdf * len(counts) * bin_width

    plt.plot(x, expected_counts, 'k-', lw=2, label='Normal fit')
    plt.title('Histogram of Final Accumulated Strand Counts')
    plt.xlabel('Accumulated Count')
    plt.ylabel('Number of Strands')
    plt.legend(fontsize=10)

    # Annotate the plot with the count of strands that have zero counts.
    zero_count = (counts == 0).sum()
    plt.text(0.05, 0.95, f"Zero count strands: {zero_count}",
             transform=plt.gca().transAxes, fontsize=12,
             verticalalignment='top')

    if filename:
        plt.savefig(filename)
    if show:
        plt.show()
    else:
        plt.close()
