// Background: A permutation of a list L is a list which contains the same elements as L, but in any order. For example, the following lists are all the permutations of [1, 2, 3]:
// [1, 2, 3]
// [1, 3, 2]
// [2, 1, 3]
// [2, 3, 1]
// [3, 1, 2]
// [3, 2, 1]
// With this in mind, write the function isPermutation(L), which takes a list L, and returns true if L is a permutation of the list of numbers from 0 to (n - 1) inclusive, and false otherwise. n is the length of L.



// Function Signature:

function isPermutation(L) {
  // Your code here
  const n = L.length;
  const seen = new Set();

  for (let i = 0; i < n; i++) {
    if (L[i] < 0 || L[i] >= n || seen.has(L[i])) {
      return false;
    }
    seen.add(L[i]);
  }
  return true;
}

// Sample Test Case 01: console.log(isPermutation([0,2,1,4,3]))

// Expected output: true


// Sample Test Case 02: console.log(isPermutation([1,3,0,4,2]))

// Expected output: true
