# Quick Sort
# Using an element "pivot", move the value smaller than pivot to the left, bigger than pivot to the right


# 1) Choose an element in the array to be a pivot
# 2) Order the rest of the array, values lower than the pivot element on the left, and higher values on the right
# 3) Swap the pivot into the first value of higher side sub-array
# 4) Repeat 2-3 recursively

# Recursion - When the function calls itself
#   => Quick sort need to call itself to each sub-arrays

# method that receives sub-array, moves value around
# low, high: index range to divide the array
def partition(arr, low, high):
    pivot = arr[high] # set pivot value as the last element in the sub-array
    i = low - 1  # i = first index the sub-array, borderline of the minimum sub-array

    for j in range(low, high): # loop around the array between low value and high value
        if arr[j] <= pivot: # found the value lower than pivot
            i += 1  # increase i
            arr[i], arr[j] = arr[j], arr[i] # bring this small value to the front

    arr[i+1], arr[high] = arr[high], arr[i+1]   # swap pivot into its final position
    return i+1  # return pivot position

    # 1) pivot value = last element of the sub-array
    # 2) i = boundary of the smaller-than-pivot region (low - 1)
    # 3) loop the array between low and high
    # 4) if value is lower than pivot, advance i and swap it into the smaller region
    # 5) lastly, swap the arr[i+1] and arr[high]
    # 6) return pivot position



def quicksort(arr, low=0, high=None):
    print(f'quicksort({arr}, {low}, {high}) called \n')
    if high is None:    # set the initial high value as the last index
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)       # set the pivot value
        quicksort(arr, low, pivot_idx - 1)      # sort low sub-array
        quicksort(arr, pivot_idx + 1, high)     # sort high sub-array


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

# Time Complexity: worst O(n^2), Average O(n*logn)
