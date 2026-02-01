"""
Experiment 8: Compare Insertion sort with Merge and Quick sort for small lists
"""

import timeit
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
    small_lengths = [ x for x in range(140)]
    algorithms_small = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": mergesort,
        "Quick Sort": quicksort
    }
    
    times_small = {name: [] for name in algorithms_small}
    runs = 400
    max_value = 2000
    
    for length in small_lengths:
        
        
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms_small}
        
        for _ in range(runs):
            L = create_random_list(length, max_value)
            for name, sort_func in algorithms_small.items():
                L_copy = L.copy()
                start = timeit.default_timer()
                sort_func(L_copy)
                end = timeit.default_timer()
                avg_times[name] += (end - start)
        
        for name in algorithms_small:
            avg_times[name] /= runs
            times_small[name].append(avg_times[name])
    
    # Plot comparison for small lists
    plt.plot(small_lengths, times_small["Insertion Sort"], label="Insertion Sort")
    plt.plot(small_lengths, times_small["Merge Sort"], label="Merge Sort")
    plt.plot(small_lengths, times_small["Quick Sort"], label="Quick Sort")
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 8: Comparison for Small Lists")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_experiment8()