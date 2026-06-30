# Insertion Sort
# 1) Consider the first element as an initial sorted part
# 2) Take the first value from the unsorted part of the array
# 3) Place the taken value into the correct place in the sorted part
# 4) Repeat 2-3 until it is sorted



my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# my implementation
sortedIdx = 0
for i in range(0, len(my_array) - 1):
    targetIdx = sortedIdx + 1
    for j in range(targetIdx):
        if my_array[targetIdx] < my_array[j]:
            my_array[targetIdx], my_array[j] = my_array[j], my_array[targetIdx]
    sortedIdx += 1
print(my_array)

# actual implementation
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(1, n):
    insert_idx = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_idx = j
    my_array.insert(insert_idx, current_value)
print(my_array)

# Consider unseen shifting operations
#   => Insert, Pop operation always shifting other elements behind the target index
#       1) Insert: insert to target index, make a space by pushing all the other elements behind it
#       2) Pop: remove the element from the array, fill in the blank by pulling all the other elements behind it
#   => which takes a lot of time, but not shown in high-level languages e.g.) Javascript, Python

# Improvements - only shifting necessary values
# 1) Copy the first non-sorted part value
# 2) Shift back indices if the copied value is smaller than them
# 3) Set the target index and paste the copied value into that index
# 4) repeat 2-3

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(1, n):
    insertIdx = i
    currentVal = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > currentVal:
            my_array[j+1] = my_array[j]
            insertIdx = j
        else:
            break
    my_array[insertIdx] = currentVal
print(my_array)

# Time Complexity = O(n/2 * n) = O(n^2)






