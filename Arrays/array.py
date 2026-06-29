my_array = [7, 12, 9, 4, 11]
# Try to write down the procedure before writing the code
# 1) create min_val/max_val stores a minimum or maximum value of the array
# 2) set the initial value(first item of the array)
# 3) while loop, compare the min/max value and each values inside the array
# 4) if the value is smaller/bigger than min/max value, replace it with min/max value
# 5) return the result

# or pseudocode
# e.g.) min: function getMinVal()
#               variable min = array[0]
#               for every elements in array
#                   if min > current element
#                       min = current element
#               return element

def get_min_val(arr):
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

def get_max_val(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

print(f'minVal = {get_min_val(my_array)} maxVal = {get_max_val(my_array)}')


# Time Complexity - how much time an algorithm takes to run
# e.g) get_min_val/get_max_val = O(N) linear (proportional to the size of the dataset

# Practice
print(my_array[0])