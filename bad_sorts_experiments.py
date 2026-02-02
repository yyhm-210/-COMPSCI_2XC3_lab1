import random
import timeit
import matplotlib.pyplot as plt
import bad_sorts_update

lengths = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
max_value = 5000
lists = [bad_sorts_update.create_random_list(_, max_value) for _ in lengths]
n = len(lengths)
runs = 20

#warm up
for _ in range(5):
    warmUp = bad_sorts_update.create_random_list(1000, 1000)
    bad_sorts_update.bubble_sort(warmUp)

    warmUp = bad_sorts_update.create_random_list(1000, 1000)
    bad_sorts_update.insertion_sort(warmUp)

    warmUp = bad_sorts_update.create_random_list(1000, 1000)
    bad_sorts_update.selection_sort(warmUp)

    warmUp = bad_sorts_update.create_random_list(1000, 1000)
    bad_sorts_update.bubble_sort_2(warmUp)

    warmUp = bad_sorts_update.create_random_list(1000, 1000)
    bad_sorts_update.selection_sort_2(warmUp)

#experiment1
bubble_sort_t = []
insertion_sort_t = []
selection_sort_t = []

for c in range(n):
    
    timer = 0.0
    for _ in range(runs):
        l_copy = list(lists[c])
        start = timeit.default_timer()
        bad_sorts_update.bubble_sort(l_copy)
        end = timeit.default_timer()
        timer += (end - start)
    bubble_sort_t.append(timer / runs)

    timer = 0.0
    for _ in range(runs):
        l_copy = list(lists[c])
        start = timeit.default_timer()
        bad_sorts_update.insertion_sort(l_copy)
        end = timeit.default_timer()
        timer += (end - start)
    insertion_sort_t.append(timer / runs)

    timer = 0.0
    for _ in range(runs):
        l_copy = list(lists[c])
        start = timeit.default_timer()
        bad_sorts_update.selection_sort(l_copy)
        end = timeit.default_timer()
        timer += (end - start)
    selection_sort_t.append(timer / runs)

plt.plot(lengths, bubble_sort_t, color='red', label="Bubble Sort")
plt.plot(lengths, insertion_sort_t, color='blue', label="insertion_sort")
plt.plot(lengths, selection_sort_t, color='green', label="selection_sort")
plt.title('Experiment 1: Runtime Comparison of Bubble, Insertion, and Selection Sort')
plt.xlabel("List length (n)")
plt.ylabel("Average runtime (s)")
plt.legend()
plt.grid(True)
plt.show()

#experiment2
bubble_sort_t2 = []
selection_sort_t2 = []

for c in range(n):
    
    timer = 0.0
    for _ in range(runs):
        l_copy = list(lists[c])
        start = timeit.default_timer()
        bad_sorts_update.bubble_sort_2(l_copy)
        end = timeit.default_timer()
        timer += (end - start)
    bubble_sort_t2.append(timer / runs)

    timer = 0.0
    for _ in range(runs):
        l_copy = list(lists[c])
        start = timeit.default_timer()
        bad_sorts_update.selection_sort_2(l_copy)
        end = timeit.default_timer()
        timer += (end - start)
    selection_sort_t2.append(timer / runs)

plt.plot(lengths, bubble_sort_t, color='red', label="Bubble_Sort")
plt.plot(lengths, bubble_sort_t2, color='blue', label="Bubble_Sort_2")
plt.title('Experiment 2_1: origin vs better bubble sort')
plt.xlabel("List length (n)")
plt.ylabel("Average runtime (s)")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(lengths, selection_sort_t, color='red', label="selection_sort")
plt.plot(lengths, selection_sort_t2, color='blue', label="selection_sort_2")
plt.title('Experiment 2_2: origin vs better selection sort')
plt.xlabel("List length (n)")
plt.ylabel("Average runtime (s)")
plt.legend()
plt.grid(True)
plt.show()

#experiment3
fixed_length = 5000
max_value = 5000
runs = 10
swaps_list = [0, 10, 50, 100, 200, 500, 1000, 2000]

bubble_sort_t3 = []
bubble_sort_t3_2 = []
insertion_sort_t3 = []
selection_sort_t3 = []
selection_sort_t3_2 = []

for swaps in swaps_list:

    bubble_timer = 0.0
    bubble_timer_2 = 0.0
    insertion_timer = 0.0
    selection_timer = 0.0
    selection_timer_2 = 0.0

    for _ in range(runs):
        L = bad_sorts_update.create_near_sorted_list(fixed_length, max_value, swaps)

        l_copy = list(L)
        start = timeit.default_timer()
        bad_sorts_update.bubble_sort(l_copy)
        end = timeit.default_timer()
        bubble_timer += (end - start)

        l_copy = list(L)
        start = timeit.default_timer()
        bad_sorts_update.insertion_sort(l_copy)
        end = timeit.default_timer()
        insertion_timer += (end - start)

        l_copy = list(L)
        start = timeit.default_timer()
        bad_sorts_update.selection_sort(l_copy)
        end = timeit.default_timer()
        selection_timer += (end - start)

        l_copy = list(L)
        start = timeit.default_timer()
        bad_sorts_update.bubble_sort_2(l_copy)
        end = timeit.default_timer()
        bubble_timer_2 += (end - start)

        l_copy = list(L)
        start = timeit.default_timer()
        bad_sorts_update.selection_sort_2(l_copy)
        end = timeit.default_timer()
        selection_timer_2 += (end - start)

    bubble_sort_t3.append(bubble_timer / runs)
    insertion_sort_t3.append(insertion_timer / runs)
    selection_sort_t3.append(selection_timer / runs)
    bubble_sort_t3_2.append(bubble_timer_2 / runs)
    selection_sort_t3_2.append(selection_timer_2 / runs)

plt.plot(swaps_list, bubble_sort_t3, color='red', label="Bubble_Sort")
plt.plot(swaps_list, bubble_sort_t3_2, color='darkred', label="better_Bubble_Sort")
plt.plot(swaps_list, insertion_sort_t3, color='blue', label="Insertion_Sort")
plt.plot(swaps_list, selection_sort_t3, color='green', label="Selection_Sort")
plt.plot(swaps_list, selection_sort_t3_2, color='limegreen', label="better_Selection_Sort")
plt.xlabel("Number of random swaps")
plt.ylabel("Runtime (s)")
plt.title("Experiment 3: Effect of Near-Sortedness on Bad Sorting Algorithms")
plt.legend()
plt.grid(True)
plt.show()