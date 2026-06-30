# Bubble Sort
# 1) Go through the array, one value at one time
# 2) For each value, compare with next item
# 3) if the current item is bigger/smaller, switch the index
# 4) repeat 1-3 until the array is sorted

# Time Complexity - O(n^2)

print(f'== Bubble Sort ==')
my_array = [ 7,12,9,11,3 ]
n = len(my_array)
for i in range(n-1):
    for j in range (n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            print(f'Step {i} = {my_array}')

print(f'result: {my_array}')

# Improvement - Swap Indicator
# if swap didn't happen, skip the rest of process => reduce redundant process
print(f'\n== Bubble Sort - Improved ==')
my_array2 = [7, 3, 9, 12, 11]

o = len(my_array2)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array2[j] > my_array2[j+1]:
            my_array2[j], my_array2[j+1] = my_array2[j+1], my_array2[j]
            swapped = True
    if not swapped:
        break
