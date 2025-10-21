// This problem is inspired by the children's game of "FizzBuzz" which is meant
// to help teach some basic arithmetic concepts.
  
// Write the function fizzBuzz(n) that takes an int n and returns:
// * 'fizz' if n is a multiple of 3,
  
// * 'buzz' if n is a multiple of 5,
  
// * 'fizzBuzz' if n is a multiple of 3 and also a multiple of 5, or
  
// * n itself if none of the other rules apply.

function fizzBuzz(n){
    if (n % 3 === 0 && n % 5 === 0) return "fizzbuzz";
    if (n % 3 === 0) return "fizz";
    if (n % 5 === 0) return "buzz";
    return n.toString();
}

// Test Function
function testFizzBuzz() {
  console.log("Testing fizzBuzz()...", "");

  // Sample Test 01
  let result1 = fizzBuzz(21);
  console.assert(result1 === "fizz", `Test 1 failed: got ${result1}`);

  // Sample Test 02
  let result2 = fizzBuzz(25);
  console.assert(result2 === "buzz", `Test 2 failed: got ${result2}`);

  // Additional sanity checks
  let result3 = fizzBuzz(15);
  console.assert(result3 === "fizzbuzz", `Test 3 failed: got ${result3}`);

  let result4 = fizzBuzz(7);
  console.assert(result4 === "7", `Test 4 failed: got ${result4}`);

  console.log("Passed!");
}

// Run the tests
testFizzBuzz();