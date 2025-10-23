// This problem is inspired by this page of probability problems.
// That page shows that the probability of getting exactly 2 heads in 5 coin flips is 0.3125.
// Your task here is to use Monte Carlo methods to estimate this probability.
// More specifically, write the function estimateProbability(trials) that runs the given number of trials, where each trial succeeds if it flips 5 coins and exactly 2 of them are heads.
// To be judged correct, you need to be reasonably close to the actual answer as the number of trials increases. See the test code for details.
// Also, note that the helper function flipCoin() has been provided for you.
// Good luck!
// Note: As you may recall, the console.assert statement in the test cases will succeed quietly if the assertion is true, and print a message only if it fails.




// Function Signature:

function flipCoin() {
    // Simulate a coin flip, returning 'H' for heads or 'T' for tails
    return Math.random() < 0.5 ? 'H' : 'T';
}

function estimateProbability(trials) {
    let successCount = 0;

    for (let i = 0; i < trials; i++) {
        let headsCount = 0;

        for (let j = 0; j < 5; j++) {
            if (flipCoin() === 'H') {
                headsCount++;
            }
        }

        if (headsCount === 2) {
            successCount++;
        }
    }

    return successCount / trials;
}






// Sample Test Case 01: const trials = 10 ** 5;
// const p = estimateProbability(trials);
// console.log(0.30 <= p && p <= 0.32);

// Expected output: true


// Sample Test Case 02: const trials = 10 ** 5;
// const p = estimateProbability(trials);
// console.log(0.305 <= p && p <= 0.32);

// Expected output: true



 
