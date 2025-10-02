"""
Background: The Levenshtein distance between two strings is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one string into the other.

If two strings are the same, their distance is 0.
If you can change one string into the other by making just one insertion, deletion, or substitution, their distance is 1.
And so on.
Happily, people have written versions of this function for us. We will use the levenshtein function from here. The starter code already includes this function for you. It takes two strings and returns their Levenshtein distance as a non-negative int.

With this in mind, write the function spellCheck(lookupWord, words) that takes two strings -- the first is a word we are looking up (that is, the word we are spell checking) and the second is a space-separated string of all the legal words.

Assume all words are lowercase.
Assume the space-separated words are in alphabetical order.
Normally, the list of words would contain thousands of words. Here, to keep testing simple, it will only contain a few words.
In any case, your function should return:

The lookupWord itself if it is included in the legal words, or
A comma-separated string of all the legal words that are closest (by Levenshtein distance) to the lookupWord, so long as their distance is not greater than 2.
None if no legal word has a distance of 2 or less to the lookupWord.
"""

def spellCheck(lookupWord, words):
    word_list = words.split()
    if lookupWord in word_list:
        return lookupWord

    closest_words = []
    min_distance = float('inf')

    for word in word_list:
        distance = levenshtein(lookupWord, word)
        if distance < min_distance:
            min_distance = distance
            closest_words = [word]
        elif distance == min_distance:
            closest_words.append(word)

    if min_distance <= 2:
        return ','.join(closest_words)
    else:
        return None

# from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def testSpellCheck():
    print('Testing spellCheck()...', end='')
    words = 'cat cow dog frog'
    assert(spellCheck('frog', words) == 'frog')     # frog is correct
    assert(spellCheck('cats', words) == 'cat')      # cat is distance 1
    assert(spellCheck('caw',  words) == 'cat,cow')  # cat and cow are distance 1
    assert(spellCheck('drog', words) == 'dog,frog') # dog and frog are distance 1
    assert(spellCheck('kit',  words) == 'cat')      # cat is distance 2
    assert(spellCheck('ack',  words) == None)       # cat, cow, and dog are
                                                    # distance 3 (too far)
    print('Passed!')

def main():
    testSpellCheck()

main()