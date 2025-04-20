# parallel_quicksort.py
from multiprocessing import Pool
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with Pool(2) as pool:
        left_right = pool.map(quicksort, [left, right])
    return left_right[0] + middle + left_right[1]

if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(100)]
    sorted_arr = quicksort(arr)
    print(sorted_arr)
