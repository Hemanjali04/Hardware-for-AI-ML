# quicksort.py
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(100)]
    sorted_arr = quicksort(arr)
    print(sorted_arr)
