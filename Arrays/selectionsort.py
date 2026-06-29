# Selection Sort
# 1) Go through the array, find the lowest value
# 2) Move the lowest value right next to the unsorted part of array
#   2-1) pop the item with minimum value
#   2-2) insert the min_val item right before the unsorted part of array(insert at index i)
# 3) repeat until the array is sorted

my_array = [ 7, 12, 9, 11, 3]
n = len(my_array)

print('== Selection Sort ==')
for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_idx]:
            min_idx = j
    min_val = my_array.pop(min_idx)     # pop the min_val
    my_array.insert(i, min_val)         # insert the min_val
    print(f'Cycle #{i + 1} : {my_array}')


print(f'result: {my_array}')

# Improvements - Swapping values
# Instead of pop-shift-insert, simply swap those values

print('\n== Selection Sort - Improved ==')
my_array2 = [ 7, 12, 9, 11, 3]
o = len(my_array2)

for i in range(o-1):
    min_idx2 = i
    for j in range(i+1, o): # range: i+1 to o (next item of minVal ~ end of array)
        if my_array2[j] < my_array2[min_idx2]: # get minVal
            min_idx2 = j
    my_array2[i], my_array2[min_idx2] = my_array2[min_idx2], my_array2[i]
    print(f'Cycle #{i + 1} : {my_array2}')