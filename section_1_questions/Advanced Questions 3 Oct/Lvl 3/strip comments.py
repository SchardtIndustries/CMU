"""
 Write the function `stripComments(code)` that takes a multiline
 string of python code and returns a new multiline string with the comments removed.
 Note: if a line contains a comment, and once that comment is removed the
 line is either empty or is only whitespace, then ignore the line entirely
 (do not include it in the result).
"""

def stripComments(code):
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        stripped_line = line.split('#')[0].rstrip()
        if stripped_line.strip() != '':
            new_lines.append(stripped_line)
    result = '\n'.join(new_lines)
    return result

def testStripComments():
    
    print('Testing stripComments()...', end='')
    code = '''\
# here's a comment!
def foo(x):
    return x + 1    # here's another one
'''
    result = '''\
def foo(x):
    return x + 1
'''
    assert(stripComments(code) == result)

    code = '''\
def g(x):
# Here are some comments
# which must be removed
# by stripComments
    return  x * 7
'''
    result = '''\
def g(x):
    return  x * 7
'''
    assert(stripComments(code) == result)

    code = """\
def doIHaveAnyComments():
    return 'No'
"""
    result = """\
def doIHaveAnyComments():
    return 'No'
"""
    assert(stripComments(code) == result)

    code = '''\
def f(x):
    #This function returns x + 5
    return x + 5
'''
    result = '''\
def f(x):
    return x + 5
'''
    assert(stripComments(code) == result)

    assert(stripComments('') == '')
    print('Passed!')

def main():
    testStripComments()

main()
