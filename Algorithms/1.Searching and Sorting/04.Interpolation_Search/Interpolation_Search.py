The formula for pos can be derived as follows.

# Let's assume that the elements of the array are linearly distributed. 

# General equation of line : y = m*x + c.
# y is the value in the array and x is its index.
"""
Now putting value of lo,hi and x in the equation
arr[hi] = m*hi+c ----(1)
arr[lo] = m*lo+c ----(2)
x = m*pos + c     ----(3)

m = (arr[hi] - arr[lo] )/ (hi - lo)

subtracting eqxn (2) from (3)
x - arr[lo] = m * (pos - lo)
lo + (x - arr[lo])/m = pos
pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])
"""



def Interpolation_search(arr, low, high, x):

    # Since array is sorted, an element present in array must be in range defined by corner.
    if (low <= high and x >= arr[low] and x <= arr[high]):
        pos = low + ((high - low)// arr[high] - arr[low])*(x - arr[low]))
