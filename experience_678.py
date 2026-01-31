"""
Experiments for good sorting algorithms (Experiments 6-8)
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np
from good_sorts_update import quicksort, mergesort, heapsort, dual_quicksort, bottom_up_mergesort

# ==================== Helper functions ====================

def create_random_list(length, max_value):
    """Generate a random list of given length with values up to max_value"""
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    """Create a nearly sorted list by making random swaps on a sorted list"""
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        i = random.randint(0, length - 1)
        j = random.randint(0, length - 1)
        L[i], L[j] = L[j], L[i]
    return L

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

def run_experiment6():
    """
    Experiment 6: Compare traditional Quick sort vs Dual Pivot Quick sort
    """
    print("Running Experiment 6...")
    
    # Test different list sizes
    lengths = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000]
    algorithms = {
        "Quick Sort": quicksort,
        "Dual Pivot Quick Sort": dual_quicksort
    }
    
    times = {name: [] for name in algorithms}
    runs = 5  # Number of repetitions for averaging
    
    for length in lengths:
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms}
        
        # Run multiple times for better average
        for _ in range(runs):
            L = create_random_list(length, 100000)
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
    plt.plot(lengths, times["Quick Sort"], label="Quick Sort")
    plt.plot(lengths, times["Dual Pivot Quick Sort"], label="Dual Pivot Quick Sort")
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 6: Traditional vs Dual Pivot Quick Sort")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')  # Logarithmic scale for better visualization
    plt.yscale('log')
    plt.show()
    
    return times, lengths

def run_experiment7():
    """
    Experiment 7: Compare traditional Merge sort vs Bottom-up Merge sort
    """
    print("Running Experiment 7...")
    
    lengths = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000]
    algorithms = {
        "Merge Sort": mergesort,
        "Bottom-up Merge Sort": bottom_up_mergesort
    }
    
    times = {name: [] for name in algorithms}
    runs = 5
    
    for length in lengths:
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms}
        
        for _ in range(runs):
            L = create_random_list(length, 100000)
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
    plt.plot(lengths, times["Merge Sort"], label="Merge Sort")
    plt.plot(lengths, times["Bottom-up Merge Sort"], label="Bottom-up Merge Sort")
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 7: Traditional vs Bottom-up Merge Sort")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
    return times, lengths

def run_experiment8():
    """
    Experiment 8: Compare Insertion sort with Merge and Quick sort for small lists
    """
    print("Running Experiment 8...")
    
    # Test small list sizes
    small_lengths = list(range(5, 101, 5)) + list(range(100, 1001, 100))
    algorithms_small = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": mergesort,
        "Quick Sort": quicksort
    }
    
    times_small = {name: [] for name in algorithms_small}
    runs = 10
    
    for length in small_lengths:
        if length > 200:
            runs = 5  # Fewer runs for larger lists
        
        print(f"  Testing length = {length}")
        avg_times = {name: 0 for name in algorithms_small}
        
        for _ in range(runs):
            L = create_random_list(length, 10000)
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
    plt.plot(small_lengths, times_small["Insertion Sort"], label="Insertion Sort")
    plt.plot(small_lengths, times_small["Merge Sort"], label="Merge Sort")
    plt.plot(small_lengths, times_small["Quick Sort"], label="Quick Sort")
    plt.xlabel("List length (n)")
    plt.ylabel("Average runtime (seconds)")
    plt.title("Experiment 8: Comparison for Small Lists")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1000)  # Focus on small list sizes
    plt.show()
    
    return {
        'small_times': times_small,
        'small_lengths': small_lengths
    }

def run_all_experiments():
    """Run all good sort experiments (6-8)"""
    print("Starting Good Sorts Experiments (6-8)...")
    print("=" * 50)
    
    results = {}
    
    # Run each experiment and store results
    results['exp6'] = run_experiment6()
    print("\n" + "=" * 50 + "\n")
    
    results['exp7'] = run_experiment7()
    print("\n" + "=" * 50 + "\n")
    
    results['exp8'] = run_experiment8()
    print("\n" + "=" * 50 + "\n")
    
    print("All experiments completed!")
    return results

if __name__ == "__main__":
    # Main entry point: run all experiments
    run_all_experiments()
    
    # Option 2: Run specific experiments individually
    # run_experiment6()  # Compare Quick Sort vs Dual Pivot Quick Sort
    # run_experiment7()  # Compare Merge Sort vs Bottom-up Merge Sort
    # run_experiment8()  # Compare Insertion, Merge, Quick Sort for small lists