// Write a program that checks whether all the digits in a given number are even.
// Input:
// A single integer N (1 ≤ N ≤ 109).
// Output:
// Print true if all the digits of N are even; otherwise, print false.
// Definition of Even Digits:
// The even digits are 0, 2, 4, 6, and 8.
// Example 1:
// Input: 2486
// Output: true
// Explanation: All the digits (2, 4, 8, 6) are even, so the output is true.
// Example 2:
// Input: 1234
// Output: false
// Explanation: The digits include 1 and 3, which are odd, so the output is false.
// Constraints:
// The program should handle the number without converting it to a string for the check.

function areAllDigitsEven(N) {
    while (N > 0) {
        let digit = N % 10; // Get the last digit
        if (digit % 2 !== 0) { // Check if the digit is odd
            return false; // If any digit is odd, return false
        }
        N = Math.floor(N / 10); // Remove the last digit
    }
    return true; // All digits are even
}

function testAreAllDigitsEven() {
  console.log("Testing areAllDigitsEven()...", "");

  // Sample Test 01
  let result1 = areAllDigitsEven(2468);
  console.assert(result1 === true, `Test 1 failed: got ${result1}`);

  // Sample Test 02
  let result2 = areAllDigitsEven(1234);
  console.assert(result2 === false, `Test 2 failed: got ${result2}`);

  // Extra sanity checks
  let result3 = areAllDigitsEven(0);
  console.assert(result3 === true, `Test 3 failed: got ${result3}`);

  let result4 = areAllDigitsEven(222222);
  console.assert(result4 === true, `Test 4 failed: got ${result4}`);

  let result5 = areAllDigitsEven(13579);
  console.assert(result5 === false, `Test 5 failed: got ${result5}`);

  console.log("Passed!");
}

// Run the tests
testAreAllDigitsEven();