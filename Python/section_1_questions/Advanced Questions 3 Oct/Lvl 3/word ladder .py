"""
Background: A word ladder is a sequence of words where adjacent words differ by only one letter. 
For example: 'dog-cog-cot-cat' is a word ladder, because 'dog' and 'cog' differ only at index 0, 'cog' 
and 'cot' differ only at index 2, and 'cot' and 'cat' differ only at index 1.

To be more precise, we will say that a string s is a word ladder if:

s is nonempty and contains at least two words, separated by dashes. Here, a 
"word" is any collection of characters that are not dashes (so words can include letters, digits, etc).
All the words in s are the same length.
Each word in s differs from the preceding word by exactly one letter (that is, at only one index).
No word appears in s more than once.
With this in mind, write the function isWordLadder(s) that takes a string s and returns True if s is a 
word ladder as just defined, and False otherwise.

Important hints:

You may want to use s.split('-') here to loop over each word in a dash-separated list of words.
While there are several ways to solve this, we found it helpful to use a variable allPrevWords that keeps 
track of every word in the word ladder up to the current word. When we are done checking the current word, we add it to 
this string, also adding dashes to the string so the words remain dash-separated. For example, during a call to 
isWordLadder('dog-cog-cot-cat'), after we checked the first 2 words, allPrevWords would then be the string 'dog-cog'.

"""

def isWordLadder(s):
    words = s.split('-')
    if len(words) < 2:
        return False
    word_length = len(words[0])
    allPrevWords = ''
    for i in range(len(words)):
        word = words[i]
        if len(word) != word_length:
            return False
        if word in allPrevWords.split('-'):
            return False
        if i > 0:
            prev_word = words[i - 1]
            diff_count = sum(1 for a, b in zip(word, prev_word) if a != b)
            if diff_count != 1:
                return False
        allPrevWords += ('-' if allPrevWords else '') + word
    return True

def testIsWordLadder():
    print('Testing isWordLadder()...', end='')
    assert(isWordLadder('dog-cog-cot-cat') == True)
    assert(isWordLadder('cat-bat') == True)
    assert(isWordLadder('cold-cord-card-ward-warm') == True)
    assert(isWordLadder('toggle-goggle-google') == True)
    assert(isWordLadder('cold-cord-card-warm') == False)
    assert(isWordLadder('cat-bat-cat') == False) # duplicate word
    assert(isWordLadder('cat-bat-') == False)
    assert(isWordLadder('cat-cats') == False)
    assert(isWordLadder('cat-cabs') == False)
    assert(isWordLadder('cat') == False) # just one word
    assert(isWordLadder('') == False) # no words
    assert(isWordLadder('-') == False) # no words
    print('Passed!')

def main():
    testIsWordLadder()

main()

