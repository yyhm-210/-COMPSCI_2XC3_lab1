import random
import timeit
import matplotlib.pyplot as plt
from bad_sorts import create_random_list
from good_sorts import heapsort, mergesort, quicksort


lengths = [1000 * x for x in range(10)]
max_value = 100
runs = 10

lists = [create_random_list(n, max_value) for n in lengths]

data_A = []
data_B = []
data_C = []

for L in lists:



    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        quicksort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_A.append(total / runs)

    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        mergesort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_B.append(total / runs)

    total = 0.0
    for _ in range(runs):
        tmp = L.copy()
        start = timeit.default_timer()
        heapsort(tmp)
        end = timeit.default_timer()
        total += (end - start)
    data_C.append(total / runs)

plt.plot(lengths, data_A, label="Quick sort")
plt.plot(lengths, data_B, label="Merge sort")
plt.plot(lengths, data_C, label="Heap sort")
plt.xlabel("List length (n)")
plt.ylabel("Average runtime (seconds)")
plt.title("Experiment 4: Runtime vs List Length (Good Sorts)")
plt.legend()
plt.grid(True)
plt.show()
