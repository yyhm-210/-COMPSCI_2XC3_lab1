"""
Experiment 8: Compare Insertion sort with Merge and Quick sort for small lists
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np
from good_sorts_update import mergesort, quicksort

# ==================== Helper functions ====================

def create_random_list(length, max_value):
    """Generate a random list of given length with values up to max_value"""
    return [random.randint(0, max_value) for _ in range(length)]

def insertion_sort(L):
    """Standard insertion sort implementation"""
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key

# ========================================================================================

def run_experiment8():
    """
    Experiment 8: Compare Insertion sort with Merge and Quick sort for small lists
    """
    print("Running Experiment 8: Comparison for Small Lists")
    print("=" * 50)
    
    # Test small list sizes
    small_lengths = list(range(5, 101, 5)) + list(range(100, 1001, 100))
    algorithms_small = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": mergesort,
        "Quick Sort": quicksort
    }
    
    times_small = {name: [] for name in algorithms_small}
    runs = 25
    max_value = 200000
    
    for length in small_lengths:
        if length > 200:
            runs = 5  # Fewer runs for larger lists
        
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms_small}
        
        for _ in range(runs):
            L = create_random_list(length, max_value)
            for name, sort_func in algorithms_small.items():
                L_copy = L.copy()
                start = time.time()
                sort_func(L_copy)
                end = time.time()
                avg_times[name] += (end - start)
        
        for name in algorithms_small:
            avg_times[name] /= runs
            times_small[name].append(avg_times[name])
    
    # Plot comparison for small lists
    plt.figure(figsize=(12, 8))
    plt.plot(small_lengths, times_small["Insertion Sort"], label="Insertion Sort", marker='o', linewidth=2)
    plt.plot(small_lengths, times_small["Merge Sort"], label="Merge Sort", marker='s', linewidth=2)
    plt.plot(small_lengths, times_small["Quick Sort"], label="Quick Sort", marker='^', linewidth=2)
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 8: Comparison for Small Lists")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1000)
    plt.show()
    
    # Print summary for key sizes
    print("\nExperiment 8 Summary (Key sizes):")
    print("=" * 40)
    key_sizes = [1, 30, 35, 50, 170, 290, 5500, 100000]
    for size in key_sizes:
        if size in small_lengths:
            idx = small_lengths.index(size)
            print(f"\nList size {size}:")
            print(f"  Insertion Sort: {times_small['Insertion Sort'][idx]:.6f} seconds")
            print(f"  Merge Sort: {times_small['Merge Sort'][idx]:.6f} seconds")
            print(f"  Quick Sort: {times_small['Quick Sort'][idx]:.6f} seconds")
    
    return {
        'small_times': times_small,
        'small_lengths': small_lengths
    }

if __name__ == "__main__":
    run_experiment8()