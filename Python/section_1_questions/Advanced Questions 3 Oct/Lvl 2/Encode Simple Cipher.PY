"""
Background: a transposition cipher is a way to encode (or encipher) a string. It works by scrambling the positions 
of the characters in the string without changing the characters themselves.

Here we will create a simple transposition cipher. Basically, this cipher swaps each character at index i with the 
character at index j = 2*i. This is performed left-to-right, starting at i=0.

One complication: if 2*i is larger than the largest index allowed (that is, len(s)-1), then it "wraps around". 
For example, if the string is of length 4, then on the third step, i = 2, and we would swap with j = 2*i = 4. 
But that is too large, so j wraps around to the beginning of the string (by subtracting the length of the string) to j = 0. 
So we swap s[2] with s[0].

Here are all the steps to encode s = 'ABCD':

Swap s[0] with s[0] to get 'ABCD'
Swap s[1] with s[2] to get 'ACBD'
Swap s[2] with s[0] to get 'BCAD' # j = 2*2 = 4, but wraps to 0
Swap s[3] with s[2] to get 'BCDA' # j = 2*3 = 6, but wraps to 2
Thus, we encode 'ABCD' to 'BCDA'.

With this in mind, write the function encodeSimpleCipher(s) that takes a string s and returns the string encoded 
according to this simple cipher.

Also, write the function decodeSimpleCipher(s) that basically runs this process in reverse -- 
it takes an encoded string s and returns the original unencoded string.
"""

def encodeSimpleCipher(s):
    chars = list(s)
    for i in range(len(chars)):
        j = 2 * i
        if j >= len(chars):
            j -= len(chars)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

def decodeSimpleCipher(s):
    chars = list(s)
    for i in range(len(chars)-1, -1, -1):
        j = 2 * i
        if j >= len(chars):
            j -= len(chars)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

def testEncodeSimpleCipher():
    print('Testing encodeSimpleCipher()...', end='')
    assert(encodeSimpleCipher('AB') == 'BA')
    assert(encodeSimpleCipher('ABC') == 'ABC')
    assert(encodeSimpleCipher('ABCD') == 'BCDA')
    assert(encodeSimpleCipher('ABCDEFGH') == 'BCFGDEHA')
    assert(encodeSimpleCipher('SECRET MESSAGE') == 'MCE SSTSAEREEG')
    assert(encodeSimpleCipher('THIS IS A LONGER SECRET MESSAGE JUST FOR YOU!') ==
                              'T  SAENG SR MGARJ  H U!SSTE TFECORIIEYSELUOOS')
    print('Passed!')

def testDecodeSimpleCipher():
    print('Testing decodeSimpleCipher()...', end='')
    assert(decodeSimpleCipher('BA') == 'AB')
    assert(decodeSimpleCipher('ABC') == 'ABC')
    assert(decodeSimpleCipher('BCDA') == 'ABCD')
    assert(decodeSimpleCipher('BCFGDEHA') == 'ABCDEFGH')
    assert(decodeSimpleCipher('MCE SSTSAEREEG') == 'SECRET MESSAGE')
    assert(decodeSimpleCipher('T  SAENG SR MGARJ  H U!SSTE TFECORIIEYSELUOOS') ==
                              'THIS IS A LONGER SECRET MESSAGE JUST FOR YOU!')
    print('Passed!')

def main():
    testEncodeSimpleCipher()
    testDecodeSimpleCipher()

main()