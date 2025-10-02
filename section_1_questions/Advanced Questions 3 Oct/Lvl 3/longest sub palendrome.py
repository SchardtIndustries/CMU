"""Background: A palindrome is a string that is the same when read forwards and backwards. For example, 'abcba' is a palindrome.

With this in mind, write the function longestSubpalindrome(s) that takes a string s and returns the longest 
palindrome that occurs in s. The palindrome can consist of any consecutive characters, not just letters. For example, 
longestSubpalindrome('ab-4-be!!!') returns 'b-4-b'.

If there is a tie, return the lexicographically larger value. In Python, a string s1 is lexicographically larger 
than a string s2 if s1 > s2. Therefore, longestSubpalindrome('abcbce') will return 'cbc' since 'cbc' > 'bcb'.

Note: This function is case-sensitive, so 'A' is not treated the same as 'a' here."""

def longestSubpalindrome(s):
    def isPalindrome(s):
        return s == s[::-1]

    longest = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if isPalindrome(substring):
                if len(substring) > len(longest) or (len(substring) == len(longest) and substring > longest):
                    longest = substring
    return longest

def testLongestSubpalindrome():
    print('Testing longestSubpalindrome()...', end='')
    assert(longestSubpalindrome('ab-4-be!!!') == 'b-4-b')
    assert(longestSubpalindrome('abcbce') == 'cbc')
    assert(longestSubpalindrome('aba') == 'aba')
    assert(longestSubpalindrome('a') == 'a')
    assert(longestSubpalindrome('abd') == 'd')
    assert(longestSubpalindrome('kP:p') == 'p')
    print('Passed!')

def main():
    testLongestSubpalindrome()

main()