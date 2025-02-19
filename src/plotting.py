import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



def plot_counts(counts, bins=50, show=True, filename=None):
    """
    Plot a histogram of the counts obtained in the final simulation round.

    Parameters:
      counts (numpy array): Array of counts for each strand.
      bins (int): Number of bins for the histogram.
      show (bool): If True, display the plot.
      filename (str): If provided, save the plot to this file.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(counts, bins=bins, edgecolor='black')
    plt.title('Histogram of Strand Counts in Final Round')
    plt.xlabel('Number of occurrences')
    plt.ylabel('Number of strands')

    if filename:
        plt.savefig(filename)
    if show:
        plt.show()
    else:
        plt.close()