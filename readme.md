# Iterative Sampling and Distribution Analysis

## Overview

This project explores the process of iterative sampling from a set of **n strands (categories)** and analyzes how the probability distribution evolves over multiple rounds. The primary objective is to observe whether the system’s distribution remains stable or shifts over time. By visualizing these changes, we can understand why the resulting counts often resemble a normal (bell) curve.

### Key Concepts:
- **n** = Number of strands (categories), in the range **10⁵ ≤ n ≤ 10⁷**.
- **M** = Sample size per round, defined as **M = c * n**, where **3 ≤ c ≤ 50**.
- **R** = Number of rounds.

At each round:
1. A sample of size **M** is drawn from the current probability distribution over **n** strands.
2. The occurrences of each strand in the sample are counted.
3. The distribution is updated based on these empirical counts.
4. The new distribution is visualized, often displaying a near-normal shape.

Over multiple rounds, this iterative sampling process helps in studying **probability drift, stability, and convergence**.
 
---

## Project Structure

```
.
├── src/
│   ├── main.py          # Main script to execute simulations
│   ├── distribution.py  # Core functions for sampling and updating distributions
│   ├── plotting.py      # Visualization utilities
├── README.md            # This documentation file
└── LICENSE              # License file
```

### File Descriptions:
- **`src/main.py`**: Entry point that runs simulations and manages iterations.
- **`src/distribution.py`**: Implements probability distribution updates and sampling functions.
- **`src/plotting.py`**: Contains visualization functions for analyzing distribution changes.

---

## Installation & Setup

### Clone the Repository:
```
git clone https://github.com/Khaledkhalil4/Iterative_Sampling_and_Distribution_Analysis.git
cd <repo-name>
```

### Install Dependencies:
Using a virtual environment (recommended):
```
python3 -m venv venv
source venv/bin/activate
pip install <Required packages listed below>
```

#### Required Packages:
- `numpy`
- `matplotlib`
- (Optional) `scipy` for additional statistical functions

---

## Usage

You can run the simulation either via command-line arguments or directly in a script.

### 1. Command-Line Execution:
```
python src/main.py --num_strands 100000 --scaling_factor 10 --rounds 20 --plot True
```
#### Arguments:
| Argument         | Description                                  | Default |
|-----------------|--------------------------------------------|---------|
| `--num_strands` | Number of strands (n).                     | 100000  |
| `--scaling_factor` | Scaling factor (c) for M = c * n, 3 ≤ c ≤ 50 | 10      |
| `--rounds`      | Number of sampling rounds (R).             | 20      |
| `--plot`        | Whether to generate distribution plots.     | True    |

### 2. Running in a Python Script:
If you prefer using a Python script or Jupyter notebook:
```python
from src.distribution import run_simulation
from src.plotting import plot_counts

# Define parameters
n = 10**5  # Choose in range 10^5 - 10^7
c = 10     # Choose between 3 and 50
M = c * n  # Sample size is a multiple of n

# Run simulation
distributions, final_counts = run_simulation(n, M, R)

# Plot results
plot_counts(final_counts)
```

#### Output Variables:
- `distributions`: A list of probability distributions after each round.
- `final_counts`: The final sampled counts used for visualization.

---

## Examples

### **Single Round Analysis:**
A single multinomial draw distributes **M** counts among **n** strands, resulting in a histogram that resembles a normal distribution for large **M**.

### **Multiple Rounds Analysis:**
- **Stable Case:** If **M** is large (e.g., 10n) and **n** is moderate (e.g., 10⁶), the distribution remains approximately uniform over iterations.
- **Drift Case:** If **M** is small (e.g., 3n), random fluctuations cause some strands to dominate after several rounds.

Each case helps illustrate how probability distributions shift over time due to iterative sampling.

---

## Theoretical Background
This project relies on fundamental probability concepts, including:
- **Central Limit Theorem (CLT)**: Explains why the sampled distribution tends to a normal shape.
- **Multinomial Distribution**: Models how sampled counts distribute across **n** categories.

### References:
- [Wikipedia: Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- **Sheldon Ross**: *Introduction to Probability Models*
- [Wikipedia: Multinomial Distribution](https://en.wikipedia.org/wiki/Multinomial_distribution)

---

## License
This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## Credits
Special thanks to the **Coding and Algorithms for Memories** course team for proposing this project.

---

