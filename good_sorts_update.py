"""
Good sorting algorithms for 2XC3 Lab 1 (Part 2)

Includes:
1) Heap Sort
2) Merge Sort (recursive)
3) Quick Sort (single pivot)
4) Dual-Pivot Quick Sort        [Experiment 6]
5) Bottom-Up Merge Sort         [Experiment 7]

Author: (based on Vincent Maccio, extended for Lab requirements)
"""

# ==================== Quick Sort ====================

def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for x in L[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# ====================================================


# ==================== Dual Pivot Quick Sort ====================
# Experiment 6

def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    if len(L) == 2:
        return L if L[0] <= L[1] else [L[1], L[0]]

    p1, p2 = L[0], L[1]
    if p1 > p2:
        p1, p2 = p2, p1

    left = []
    middle = []
    right = []

    for x in L[2:]:
        if x < p1:
            left.append(x)
        elif x > p2:
            right.append(x)
        else:
            middle.append(x)

    return (
        dual_quicksort_copy(left)
        + [p1]
        + dual_quicksort_copy(middle)
        + [p2]
        + dual_quicksort_copy(right)
    )

# ====================================================


# ==================== Merge Sort (Recursive) ====================

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    mergesort(left)
    mergesort(right)

    merged = merge(left, right)
    for i in range(len(L)):
        L[i] = merged[i]


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            result.append(right[j])
            j += 1
        elif j >= len(right):
            result.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result

# ====================================================


# ==================== Bottom-Up Merge Sort ====================
# Experiment 7

def bottom_up_mergesort(L):
    n = len(L)
    width = 1

    while width < n:
        for i in range(0, n, 2 * width):
            left = L[i:i + width]
            right = L[i + width:i + 2 * width]
            merged = merge(left, right)
            L[i:i + len(merged)] = merged
        width *= 2

# ====================================================


# ==================== Heap Sort ====================

def heapsort(L):
    heap = Heap(L)
    for i in range(len(L) - 1, -1, -1):
        L[i] = heap.extract_max()


class Heap:
    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < self.length and self.data[l] > self.data[largest]:
            largest = l
        if r < self.length and self.data[r] > self.data[largest]:
            largest = r

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_val = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_val

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

# ====================================================