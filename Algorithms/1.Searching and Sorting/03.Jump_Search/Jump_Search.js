function Jump_search(arr, x, n) {
  let prev = 0;
  let step = Math.sqrt(n);

  while (arr[Math.min(step, n) - 1] < x) {
    prev = step;
    step += Math.sqrt(n);
    if (prev >= n) return -1;
  }
  // Doing a linear search for x in block beginning with prev
  while (arr[prev] < x) {
    prev++;
    if (arr[prev] == x) {
      return prev;
    }
  }
  return -1;
}

// Driver program to test function
let arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];
let x = 55;
let n = arr.length;

// Find the index of 'x' using Jump Search
let index = Jump_search(arr, x, n);

// Print the index where 'x' is located
console.log(`Number ${x} is at index ${index}`);
