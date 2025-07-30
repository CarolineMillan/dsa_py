----------------------------------------
----------- BUBBLE SORT -----------------
----------------------------------------

def bubble_sort(nums):
    # O(n^2). very slow sorting algo. while loop means that if the list is in reverse order, then the last element needs to move n places to the beginning of the list, and so the while loop will execute n times. Bubble sort loops through a list and compares two values at a time, and swapping them if needed. It keeps looping through the list comparing two elements at a time until it loops through the whole list without changing anything. Do not use this. Apparently it's east to write and understand and that's why it's famous. But it performs really badly.

    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        end -= 1
    return nums

----------------------------------------
----------- MERGE SORT -----------------
----------------------------------------

def merge_sort(nums):
    # O(nlog(n)). This is acceptably fast but memory intensive. Again, it's a learning exercise. It is also a stable sort (google it, it's a good thing). However, it uses recursion which isn't great for performance in some languages (including python)
    if len(nums) < 2:
        return nums
    first = nums[:len(nums)//2]
    second = nums[len(nums)//2:]
    sorted_first = merge_sort(first)
    sorted_second = merge_sort(second)
    sorted_nums = merge(sorted_first, sorted_second)
    return sorted_nums

def merge(first, second):
    final = []
    i = 0
    j = 0
    
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    # we're tracking the indices so we can use them to add the extra values to the final list
    if j != len(second):
        for elj in second[j:]:
            final.append(elj)

    if i != len(first):
        for eli in first[i:]:
            final.append(eli)
    
    return final

----------------------------------------
----------- INSERTION SORT -----------------
----------------------------------------

def insertion_sort(nums):
    # O(n^2). Takes ages usually but has a niche case where it's actually faster than merge sort. This is used for small collections that are mostly already sorted. If the array is completely sorted then it has a time complexity of O(n). The more sorted the input array is, the closer to O(n) it is.
    for i in range(1,len(nums)):
        j = i
        while (j > 0) and (nums[j-1] > nums[j]):
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

----------------------------------------
----------- QUICK SORT -----------------
----------------------------------------

def quick_sort(nums, low, high):
    # O(nlog(n)) on average, but it can degrade to O(n^2) if the list is already sorted. partition() is O(n) so it depends on how many times this is called, which depends on the pivot values, which depend on how sorted the list already is. Best case scenario, the pivot is the middle element in each sublist so partition() is called log(n) times. To almost ensure that quicksort is O(nlog(n)), we can shuffle the input list so that it's probably not sorted at all any more. This can be done using randomness, or by taking the median of three elements in a partition (e.g. low middle high) and the median of them is chosen to be the pivot. I don't think I've used that approach here, but all you'd have to do is change the way you choose the new pivot in partition (instead of i+1 it would be the median). Merge sort is more stable. (unstable = can change the order of elements with equal value. i.e. if there are two 5s in the array then quick sort does not preserve the order of the 5s and could potentially swap them. merge sort would preserve the order of the 5s.)
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle-1)
        quick_sort(nums, middle+1, high)


def partition(nums, low, high):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if nums[j] < nums[pivot]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
    return i+1
    
----------------------------------------
----------- SELECTION SORT -----------------
----------------------------------------

def selection_sort(nums):
    # O(n^2). Almost a bubble sort but you only do one swap per iteration of the inner loop, so it's slightly more efficient
    for i in range(0, len(nums)):
        smallest_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
    
