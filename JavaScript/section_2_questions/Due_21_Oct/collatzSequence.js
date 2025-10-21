//Starting with any positive integer N, the Collatz sequence is defined as corresponding to n as the numbers formed by the following operations :
 
// If n is even, then n = n / 2.
// If n is odd, then n = 3*n + 1.
// If you keep repeating the above steps, you will find that eventually the pattern '4, 2, 1' keeps repeating itself.
// For this program, end it when you get the first '4, 2, 1'.
// Input : 3
// Output : 3, 10, 5, 16, 8, 4, 2, 1       

// Input : 6
// Output : 6, 3, 10, 5, 16, 8, 4, 2, 1

function collatzSequence(n) {
  let seq = [n];
  while (true) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    seq.push(n);

    // Stop when the last three numbers are 4, 2, 1
    let len = seq.length;
    if (len >= 3 && seq[len - 3] === 4 && seq[len - 2] === 2 && seq[len - 1] === 1) {
      break;
    }
  }
  return seq;
}

function testCollatz() {
  console.log("Testing collatzSequence()...", "");

  function arraysEqual(a, b) {
    return (
      Array.isArray(a) &&
      Array.isArray(b) &&
      a.length === b.length &&
      a.every((val, index) => val === b[index])
    );
  }

  // Sample Test Case 01
  let result1 = collatzSequence(3);
  console.assert(arraysEqual(result1, [3, 10, 5, 16, 8, 4, 2, 1]), "Test 1 failed");

  // Sample Test Case 02
  let result2 = collatzSequence(1);
  console.assert(arraysEqual(result2, [1, 4, 2, 1]), "Test 2 failed");

  // Sample Test Case 03
  let result3 = collatzSequence(4);
  console.assert(arraysEqual(result3, [4, 2, 1]), "Test 3 failed");

  let input = 3;
  collatzSequence(input);
  console.assert(input === 3, "Function should not modify input");

  console.log("Passed!");
}

// Run the tests
testCollatz();

