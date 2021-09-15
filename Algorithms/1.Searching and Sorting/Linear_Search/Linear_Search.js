// Linear Search
// Difficulty Level : Basic
// Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

/*
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
*/

// The time complexity of the above algorithm is "O(n)".

// Linear search is rarely used practically because other search algorithms
// such as the binary search algorithm and hash tables allow significantly
// faster-searching comparison to Linear search.

function Linear_search(arr, x) {
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

idx1 = Linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 50);
console.log(idx1);

// Improve Linear Search Worst-Case Complexity (如何降低複雜度)

// if element Found at last  O(n) to O(1)
// if element Not found O(n) to O(n/2)

function Linear_search_improve(arr, x) {
  let LEFT = 0;
  let RIGHT = arr.length;
  let POSITION = -1;
  for (let i = 0; i <= arr.length - 1; i++) {
    if (arr[LEFT] == x) {
      POSITION = LEFT;
    }
    if (arr[RIGHT] == x) {
      POSITION = RIGHT;
    }
    LEFT++;
    RIGHT--;
  }
  return POSITION;
}

idx2 = Linear_search_improve([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 60);
console.log(idx2);
