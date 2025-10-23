// Note: you may not use for or while loops here. Instead, use recursion.

// With that in mind, write the recursive function oddSum(L) that takes a list L of integers, and returns the sum of just the odd integers in L.

// For example, oddSum([2,3,4,3,6]) returns 6 (3+3).

// If there are no odd values in the list, return 0.




// Function Signature:

function oddSum(L) {
    // write your code here
    if (L.length === 0) {
        return 0;
    }
    if (L[0] % 2 !== 0) {
        return L[0] + oddSum(L.slice(1));
    } else {
        return oddSum(L.slice(1));
    }
}







// Sample Test Case 01: console.log(oddSum([ ]))

// Expected output: 0




// Sample Test Case 01:console.log(oddSum([1,2,3,4,5,4,3]))

// Expected output: 12