# 1. Compare x with the middle element.
# 2. If x matches with the middle element, we return the mid index.
# 3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
# 4. Else (x is smaller) recur for the left half.

def Binary_search(arr, left, right, x):
    if right >= 1:
        mid = left + (right -1) //2
        if arr[mid] > x:
            right = mid - 1
            return Binary_search(arr, left, right, x)
        elif arr[mid] < x:
            left =  mid + 1 
            return Binary_search(arr, left, right, x)
        else:
            return mid
    else:
        return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
  
# Function call
result = Binary_search(arr, 0, len(arr)-1, x)
print(result)


# --------------------------------------------------------------#
# Iterative implementation of Binary Search

def binarySearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore right half
        else:
            right = mid - 1
    # If we reach here, then the element
    # was not present
    return -1
  
# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
  
# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")