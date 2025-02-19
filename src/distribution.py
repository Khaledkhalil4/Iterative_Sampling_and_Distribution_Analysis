import matplotlib.pyplot as plt

def plot_counts(counts, bins=50, show=True, filename=None):

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
