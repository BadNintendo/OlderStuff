// Checks if an array is sorted
const isSorted = arr => arr.every((val, i) => i === 0 || val >= arr[i - 1]);

// Shuffles the array until sorted
const bogoSort = arr => {
  while (!isSorted(arr)) arr.sort(() => Math.random() - 0.5);
  return arr;
};

// Generates an array with random integers
const generateRandomArray = (size, min, max) =>
  Array.from({ length: size }, () => Math.floor(Math.random() * (max - min + 1)) + min);

// Example usage
const size = 10, minVal = 1, maxVal = 100;
const randomArray = generateRandomArray(size, minVal, maxVal);
console.log("Unsorted array:", randomArray);
console.log("Sorted array:", bogoSort(randomArray));