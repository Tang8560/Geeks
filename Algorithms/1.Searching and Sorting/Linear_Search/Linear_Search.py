# Linear Search
# Difficulty Level : Basic
# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

"""
Examples :  

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
"""

# The time complexity of the above algorithm is "O(n)". 

# Linear search is rarely used practically because other search algorithms 
# such as the binary search algorithm and hash tables allow significantly 
# faster-searching comparison to Linear search.


def Linear_search(arr, x):
    for _ in arr:
        if x == _:
            idx = arr.index(_)
            return idx
    return -1

idx = Linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 175)
print(idx)


# Improve Linear Search Worst-Case Complexity (如何降低複雜度)

# if element Found at last  O(n) to O(1)
# if element Not found O(n) to O(n/2)


def Linear_serach_improve(arr, x):
    LEFT     = 0
    RIGHT    = len(arr) -1 
    LENGTH   = len(arr)
    POSITION = -1

    for _ in range(LENGTH):
        if arr[LEFT] == x :
            POSITION = LEFT
            return POSITION
        if arr[RIGHT] == x :
            POSITION = RIGHT
            return POSITION
        LEFT  += 1
        RIGHT -= 1
    return POSITION

idx = Linear_serach_improve([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 100)
print(idx)
