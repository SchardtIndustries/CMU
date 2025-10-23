// Note: You may not use for or while loops here. Instead, use recursion.
// With that in mind, write the recursive function maxDigit(n) that takes a possibly-negative number n and returns the largest digit in n.
// For example, maxDigit(-583) returns 8.



// Function Signature:

function maxDigit(n){
    //write your code here
    n = Math.abs(n);
    const str = n.toString();
    const max = (str) => {
        if (str.length === 1) return parseInt(str);
        const current = parseInt(str[0]);
        const rest = max(str.slice(1));
        return Math.max(current, rest);
    };
    return max(str);
}





// Sample Test Case 01: console.log(maxDigit(-583))

// Expected output: 8




// Sample Test Case 01: console.log(maxDigit(1))

// Expected output: 1