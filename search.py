def binary_search(target, arr):
    # O(log(n)). works on a pre-sorted list of elements arr to find target
    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
