// Problem Statement: Movie Awards Count
// You are tasked with developing a function that counts the number of awards won by various movies based on the results from an awards ceremony. Each result indicates a specific category and the corresponding winning movie. Your function should take this input and return a summary of how many awards each movie has received.
// Function Signature:

function movieAwards(oscarResults) {
    // Write your code here
    const awardCount = {};

    for (let i = 0; i < oscarResults.length; i++) {
        const [category, movie] = oscarResults[i];
        if (awardCount[movie]) {
            awardCount[movie] += 1;
        } else {
            awardCount[movie] = 1;
        }
    }

    return awardCount;
}



// Input:
// - oscarResults: An array of tuples (represented as arrays in JavaScript), where each tuple contains:
//   - A string representing the name of the award category (e.g., "Best Picture").
//   - A string representing the name of the winning movie (e.g., "Green Book").
// Output:
// - The function should return an object (dictionary) that maps each movie name to the number of awards it has won. The keys in the object are the movie names, and the values are integers representing the count of awards.
// Constraints:
// - The input may contain multiple tuples, and each movie can win multiple awards across different categories.
// - The output should accurately reflect the total number of awards for each movie.
// - The order of the properties in the output object may vary, as JavaScript objects are unordered.
// Example:
// const oscarResults = [
//     ["Best Picture", "Green Book"], 
//     ["Best Actor", "Bohemian Rhapsody"],
//     ["Best Actress", "The Favourite"],
//     ["Film Editing", "Bohemian Rhapsody"],
//     ["Best Original Score", "Black Panther"],
//     ["Costume Design", "Black Panther"],
//     ["Sound Editing", "Bohemian Rhapsody"],
//     ["Best Director", "Roma"]
// ];
// const result = movieAwards(oscarResults);
// console.log(result);
// /*
// Expected Output:
// {
//     "Green Book": 1,
//     "Bohemian Rhapsody": 3,
//     "The Favourite": 1,
//     "Black Panther": 2,
//     "Roma": 1
// }
// */
// Notes:
// - Ensure that your function handles the case where a movie has not won any awards by not including it in the output.
// - The function should be efficient and handle a reasonable number of awards without performance issues.


// Sample Test Case 01: let test = new Set([
//         ['Best Picture', 'The Shape of Water'],
//         ['Best Actor', 'Darkest Hour'],
//         ['Best Actress', 'Three Billboards Outside Ebbing, Missouri'],
//         ['Best Director', 'The Shape of Water']
//     ]);
// console.log(movieAwards(test));

// Expected output: {
//   'The Shape of Water': 2,
//   'Darkest Hour': 1,
//   'Three Billboards Outside Ebbing, Missouri': 1
// }



// Sample Test Case 02: let test = new Set([
//     ['Best Picture', 'Spotlight'],
//     ['Best Director', 'The Revenant'],
//     ['Best Actor', 'The Revenant'],
//     ['Best Actress', 'Room'],
//     ['Best Supporting Actor', 'Bridge of Spies'],
//     ['Best Supporting Actress', 'The Danish Girl'],
//     ['Best Original Screenplay', 'Spotlight'],
//     ['Best Adapted Screenplay', 'The Big Short'],
//     ['Best Production Design', 'Mad Max: Fury Road'],
//     ['Best Cinematography', 'The Revenant']
// ]);

// console.log(movieAwards(test));


// Expected output: {
//   Spotlight: 2,
//   'The Revenant': 3,
//   Room: 1,
//   'Bridge of Spies': 1,
//   'The Danish Girl': 1,
//   'The Big Short': 1,
//   'Mad Max: Fury Road': 1
// }
