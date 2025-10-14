"""Write the function wrapText(text, lineSize) that takes a string of text 
and a lineSize, and returns a string made of the words in the original text, but where each word 
is separated by just one space (no matter how many spaces were in the original text), and where each line has exactly 
lineSize characters.

To make this easier to understand (and debug, and autograde), the returned string actually includes a vertical bar 
(|) on each end of each line, so that each line technically has (lineSize + 2) characters.

When wrapping a line, add as many spaces on the right end of the line as necessary to get to lineSize total characters 
on the line (not counting the vertical bars on each side)."""

def wrapText(text, lineSize):
    words = text.split()
    wrapped_lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + (1 if current_line else 0) <= lineSize:
            if current_line:
                current_line += " "
            current_line += word
        else:
            wrapped_lines.append(f"|{current_line.ljust(lineSize)}|")
            current_line = word

    if current_line:
        wrapped_lines.append(f"|{current_line.ljust(lineSize)}|")

    return "\n".join(wrapped_lines)

def testWrapText():
    print('Testing wrapText()...', end='')
    text = '''\
This is some sample text. It is just sample text.
Nothing more than sample text. Really, that's it.'''

    textWrappedAt20 = '''\
|This is some sample |
|text. It is just    |
|sample text. Nothing|
|more than sample    |
|text. Really, that's|
|it.                 |'''

    assert(wrapText(text, 20) == textWrappedAt20)

    textWrappedAt30 = '''\
|This is some sample text. It  |
|is just sample text. Nothing  |
|more than sample text. Really,|
|that's it.                    |'''

    assert(wrapText(text, 30) == textWrappedAt30)

    textWrappedAt40 = '''\
|This is some sample text. It is just    |
|sample text. Nothing more than sample   |
|text. Really, that's it.                |'''

    assert(wrapText(text, 40) == textWrappedAt40)
    print('Passed!')

testWrapText()