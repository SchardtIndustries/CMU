// Write the function repeats(L) which takes a list L and returns a sorted list of all the repeated elements in L.
// For example, if L = [1,2,3,2,1], then the repeated elements are 2 and 1. We return a sorted list of these elements, so repeats([1,2,3,2,1]) == [1, 2].
// Note: Recall that in this unit, you cannot create new lists or mutate existing lists. Instead, think of a clever way to use sets to solve the problem.
// Hints:
// You may want to use two sets here as you loop over all the values in the list L -- one set to keep track of the values you have already seen at least once, and another set to keep track of the values you have seen at least twice (that is, the duplicates in L).
// Recall that you can use sorted(s) here to convert a set into a sorted list of the values in that set.


// Function Signature:

function repeats(L) {
    //Write your code here
    let seenOnce = new Set();
    let seenTwice = new Set();

    for (let i = 0; i < L.length; i++) {
        if (seenOnce.has(L[i])) {
            seenTwice.add(L[i]);
        } else {
            seenOnce.add(L[i]);
        }
    }

    return sorted(seenTwice);
}

// Sample Test Case 01: console.log(repeats([1,2,3,2,1]))

// Expected output: [ 1, 2 ]


// Sample Test Case 02: console.log(repeats([1,2,3,2,2,4]))

// Expected output: [ 2 ]
