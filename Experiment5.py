import random
import timeit
import matplotlib.pyplot as plt

from bad_sorts import  create_near_sorted_list
from good_sorts_update import quicksort, mergesort, heapsort
import sys
sys.setrecursionlimit(20000)

length = 2000
max_value = 20000
runs = 50

swaps_values = [2**x for x in range(10)]

data_quick = []
data_merge = []
data_heap = []

for swaps in swaps_values:

    L = create_near_sorted_list(length, max_value, swaps)

    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        quicksort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_quick.append(total / runs)

    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        mergesort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_merge.append(total / runs)

    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        heapsort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_heap.append(total / runs)

plt.plot(swaps_values, data_quick, label="Quick sort")
plt.plot(swaps_values, data_merge, label="Merge sort")
plt.plot(swaps_values, data_heap, label="Heap sort")
plt.xlabel("Number of swaps")
plt.ylabel("Average runtime ")
plt.title("Experiment 5: Runtime vs Swaps")
plt.legend()
plt.grid(True)
plt.show()
