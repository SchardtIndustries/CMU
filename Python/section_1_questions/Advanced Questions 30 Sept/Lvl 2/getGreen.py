def getGreen(rgb):
    s = str(rgb).zfill(9)
    green = int(s[3:6])
    return green

def testGetGreen():
    print('Testing getGreen()...', end='')
    assert(getGreen(218112214) == 112)
    assert(getGreen(134134134) == 134)
    assert(getGreen(111019213) == 19)
    assert(getGreen(221000000) == 0)
    assert(getGreen(32175) == 32)
    assert(getGreen(0) == 0)
    print('Passed!')

def main():
    testGetGreen()

main()