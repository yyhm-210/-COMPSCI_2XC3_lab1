"""
Experiment 6: Compare traditional Quick sort vs Dual Pivot Quick sort
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np
from good_sorts_update import quicksort, dual_quicksort

# ==================== Helper functions ====================

def create_random_list(length, max_value):
    """Generate a random list of given length with values up to max_value"""
    return [random.randint(0, max_value) for _ in range(length)]

# ========================================================================================

def run_experiment6():
    """
    Experiment 6: Compare traditional Quick sort vs Dual Pivot Quick sort
    """
    print("Running Experiment 6: Traditional vs Dual Pivot Quick Sort")
    print("=" * 50)
    
    # Test different list sizes
    lengths = [128, 512, 1024, 8192, 16384, 32768, 65536, 131072]
    algorithms = {
        "Quick Sort": quicksort,
        "Dual Pivot Quick Sort": dual_quicksort
    }
    
    times = {name: [] for name in algorithms}
    runs = 20  # Number of repetitions for averaging
    max = 100000
    
    for length in lengths:
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms}
        
        # Run multiple times for better average
        for _ in range(runs):
            L = create_random_list(length, max)
            for name, sort_func in algorithms.items():
                L_copy = L.copy()
                start = time.time()
                sort_func(L_copy)
                end = time.time()
                avg_times[name] += (end - start)
        
        # Calculate average time for each algorithm
        for name in algorithms:
            avg_times[name] /= runs
            times[name].append(avg_times[name])
    
    # Create plot comparing the two algorithms
    plt.figure(figsize=(12, 8))
    plt.plot(lengths, times["Quick Sort"], label="Quick Sort", marker='o', linewidth=2)
    plt.plot(lengths, times["Dual Pivot Quick Sort"], label="Dual Pivot Quick Sort", marker='s', linewidth=2)
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 6: Traditional vs Dual Pivot Quick Sort")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')  # Logarithmic scale for better visualization
    plt.yscale('log')
    plt.show()
    
    # Print summary
    print("\nExperiment 6 Summary:")
    print("=" * 30)
    for i, length in enumerate(lengths):
        print(f"List size {length}:")
        print(f"  Quick Sort: {times['Quick Sort'][i]:.6f} seconds")
        print(f"  Dual Pivot: {times['Dual Pivot Quick Sort'][i]:.6f} seconds")
    
    return times, lengths

if __name__ == "__main__":
    run_experiment6()