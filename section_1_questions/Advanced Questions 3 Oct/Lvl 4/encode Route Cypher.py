"""_summary_
Note: This writeup discusses a 2-dimensional grid, but the grid is only conceptual. Your code will never 
actually construct a 2-dimensional grid (especially as you may not yet use lists!). Instead, you should use a 
clever scheme of indexing the message string where you translate a row and column into a single index into the message string.

Background: We have seen several ciphers, which encrypt a message. Here, we will consider a right-left route cipher, 
which is a bit more involved than the other ciphers we have seen so far.
A right-left route cipher takes two values, some plaintext and a number of rows, and 
(conceptually) constructs a grid with that number of rows and the minimum number of columns required, writing the 
message in successive columns. For example, if the message is ASECRETMESSAGE, with four rows, the grid would be:

A R E G
S E S E
E T S
C M A
We will assume the message only contains uppercase letters. We'll fill in the missing grid entries 
with lowercase letters starting from z and going in reverse (wrapping around if necessary), so we have:

A R E G
S E S E
E T S z
C M A y
Next, we encrypt the text by reading alternating rows first to the right ('AREG'), 
then to the left ('ESES'), then back to the right ('ETSz'), and back to the left ('yAMC'), 
until we finish all rows. We precede these encrypted values with the number of rows itself in the string. 
So the encrypted value for the message ASECRETMESSAGE with 4 rows is '4AREGESESETSzyAMC'.

With this in mind, write the function encodeRouteCipher(message, rows), which takes an all-uppercase 
message and a positive integer number of rows, and returns the encoding as just described.

Here are a few more examples to consider:

assert(encodeRouteCipher('ASECRETMESSAGE',3) == '3ACTSGESMRSEEEAz')
assert(encodeRouteCipher('ASECRETMESSAGE',5) == '5AESATSEMGEECRSz')
assert(encodeRouteCipher('ANOTHERSECRET',4) ==  '4AHETzCENORRyxEST')
Be sure to take the time to fully understand each of those examples!

Reminder: The grid described above is only conceptual. Your code will never actually construct a 
2-dimensional grid. Instead, you should translate a row and column into a single index into the message string.

More Complete Hint: Let's do this example in a bit more detail, and we'll even provide an idea or two on 
how to simplify solving this:


assert(encodeRouteCipher("ASECRETMESSAGE",3) == "3ACTSGESMRSEEEAz")
Find the dimensions of the conceptual 2d grid.
Since len('ASECRETMESSAGE') is 14, and we have 3 rows, we need math.ceil(14/3), 
or 5, columns. 2. Pad the string.

We need 3*5, or 15 letters. We have 14, so we have to add one letter. So now, our string 
is 'ASECRETMESSAGEz'. 3. Imagine the conceptual 2d grid.

We do not create this part. We just imagine it. But this is the 2d grid we imagine:

A C T S G
S R M S E
E E E A z
Label your rows and cols.
To be sure we are visualizing the grid properly, let's add row and col labels, like so:

        col0  col1  col2  col3  col4
row0:    A     C     T     S     G
row1:    S     R     M     S     E
row2:    E     E     E     A     z
Label the padded string with row, col, and i.
Let's use these row and col labels, but write them over the padded string (instead of the conceptual 
2d grid). We'll also include the index i, like so:

row:  0  1  2  0  1  2  0  1  2  0  1  2  0  1  2
col:  0  0  0  1  1  1  2  2  2  3  3  3  4  4  4
i:    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
      A  S  E  C  R  E  T  M  E  S  S  A  G  E  z
Find a function f(row, col) -- > i
Look at the patterns in the row, col, and i in the table we just made. See if you can find a 
function f(row, col) which takes any row and col (in the conceptual 2d grid) and returns the corresponding 
index i (in the padded string). Also, name this function something better than f. * Hint: From the table above, 
we see that the M is in row 1 and column 2, and the M is at index 7 in the padded string, so ... f(1, 2) == 7. 
* Hint: See how the row in the table above repeats: 0, 1, 2, 0, 1, 2, ... What does this have to do with the fact that 
we have 3 total rows? 7. Now, traverse the 2d grid top-to-bottom, left-to-right.

This step is not required, but it is super helpful. As only a temporary measure, we will solve a slightly easier version 
of the problem: we will simply ignore that every other row goes right-to-left. We'll make every row go left-to-right 
just for now. So use two loops, one going over every row, and inside that, one going over every column. For each row, 
col pair, use your function f that you just wrote (and renamed) to find the index in the padded string. Remember that this 
was the conceptual grid:

ACTSG
SRMSE
EEEAz
And so, when you are done with this step, you should have a string like this 
(which, again, is not the real solution, since we always go left-to-right):

ACTSGSRMSEEEEAz
Now alternate left-to-right and right-to-left.
Now make every other row go the opposite direction, so the second row will change from SRMSE to ESMRS, like so:

ACTSGESMRSEEEAz
Add the rows as a prefix.
Easy enough:

3ACTSGESMRSEEEAz
Return that string.
We are done. To remind ourselves, here was the test case:

assert(encodeRouteCipher("ASECRETMESSAGE",3) == "3ACTSGESMRSEEEAz")
Whew! And now that you have written the encoder, we need to write the decoder. 
For that, write the function decodeRouteCipher(encodedMessage), which takes an encoding from the 
previous problem and runs it in reverse, returning the plaintext that generated the encoding. For 
example, decodeRouteCipher('3ACTSGESMRSEEEAz') returns 'ASECRETMESSAGE'.
"""

import math, string

def encodeRouteCipher(message, rows):
    cols = math.ceil(len(message) / rows)
    total_length = rows * cols
    padding_needed = total_length - len(message)
    padding_chars = []
    for i in range(padding_needed):
        padding_chars.append(chr(ord('z') - (i % 26)))
    padded_message = message + ''.join(padding_chars)
    encoded_message = str(rows)
    for r in range(rows):
        if r % 2 == 0:  # Left to right
            for c in range(cols):
                index = r + c * rows
                encoded_message += padded_message[index]
        else:  # Right to left
            for c in range(cols - 1, -1, -1):
                index = r + c * rows
                encoded_message += padded_message[index]
    
    return encoded_message

def decodeRouteCipher(encodedMessage):
    rows = int(encodedMessage[0])
    cols = (len(encodedMessage) - 1) // rows
    grid = [[''] * cols for _ in range(rows)]
    index = 1
    for r in range(rows):
        if r % 2 == 0:  # Left to right
            for c in range(cols):
                grid[r][c] = encodedMessage[index]
                index += 1
        else:  # Right to left
            for c in range(cols - 1, -1, -1):
                grid[r][c] = encodedMessage[index]
                index += 1
    decoded_message = ''
    for c in range(cols):
        for r in range(rows):
            decoded_message += grid[r][c]
    decoded_message = decoded_message.rstrip(string.ascii_lowercase)

    return decoded_message

def testEncodeRouteCipher():
    print('Testing encodeRouteCipher()...', end='')
    assert(encodeRouteCipher('ASECRETMESSAGE', 4) == '4AREGESESETSzyAMC')
    assert(encodeRouteCipher('ASECRETMESSAGE', 3) == '3ACTSGESMRSEEEAz')
    assert(encodeRouteCipher('ASECRETMESSAGE', 5) == '5AESATSEMGEECRSz')
    assert(encodeRouteCipher('ANOTHERSECRET', 4) ==  '4AHETzCENORRyxEST')

def testDecodeRouteCipher():
    print('Testing decodeRouteCipher()...', end='')
    assert(decodeRouteCipher('4AREGESESETSzyAMC') == 'ASECRETMESSAGE')
    assert(decodeRouteCipher('3ACTSGESMRSEEEAz') ==  'ASECRETMESSAGE')
    assert(decodeRouteCipher('5AESATSEMGEECRSz') ==  'ASECRETMESSAGE')
    assert(decodeRouteCipher('4AHETzCENORRyxEST') == 'ANOTHERSECRET')
    message = 'SECRETSTUFFGOESHERE'
    encodedMessage = encodeRouteCipher(message, 6)
    plaintext = decodeRouteCipher(encodedMessage)
    assert(plaintext == message)
    print('Passed!')

def main():
    testEncodeRouteCipher()
    testDecodeRouteCipher()

main()