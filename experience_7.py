"""
Experiment 7: Compare traditional Merge sort vs Bottom-up Merge sort
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np
from good_sorts_update import mergesort, bottom_up_mergesort

# ==================== Helper functions ====================

def create_random_list(length, max_value):
    """Generate a random list of given length with values up to max_value"""
    return [random.randint(0, max_value) for _ in range(length)]

# ========================================================================================

def run_experiment7():
    """
    Experiment 7: Compare traditional Merge sort vs Bottom-up Merge sort
    """
    print("Running Experiment 7: Traditional vs Bottom-up Merge Sort")
    print("=" * 50)
    
    lengths = [256, 512, 1024, 8192, 16384, 32768, 131072, 262144]
    algorithms = {
        "Merge Sort": mergesort,
        "Bottom-up Merge Sort": bottom_up_mergesort
    }
    
    times = {name: [] for name in algorithms}
    runs = 15
    Max = 200000
    
    for length in lengths:
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms}
        
        for _ in range(runs):
            L = create_random_list(length, Max)
            for name, sort_func in algorithms.items():
                L_copy = L.copy()
                start = time.time()
                sort_func(L_copy)
                end = time.time()
                avg_times[name] += (end - start)
        
        for name in algorithms:
            avg_times[name] /= runs
            times[name].append(avg_times[name])
    
    # Plot results for comparison
    plt.figure(figsize=(12, 8))
    plt.plot(lengths, times["Merge Sort"], label="Merge Sort", marker='o', linewidth=2)
    plt.plot(lengths, times["Bottom-up Merge Sort"], label="Bottom-up Merge Sort", marker='s', linewidth=2)
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 7: Traditional vs Bottom-up Merge Sort")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
    # Print summary
    print("\nExperiment 7 Summary:")
    print("=" * 30)
    for i, length in enumerate(lengths):
        print(f"List size {length}:")
        print(f"  Merge Sort: {times['Merge Sort'][i]:.6f} seconds")
        print(f"  Bottom-up: {times['Bottom-up Merge Sort'][i]:.6f} seconds")
    
    return times, lengths

if __name__ == "__main__":
    run_experiment7()