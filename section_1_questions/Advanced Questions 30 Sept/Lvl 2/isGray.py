def isGray(rgb):
    if rgb < 0 or rgb > 255255255:
        return False
    num_str = str(rgb)
    if len(num_str) < 9:
        num_str = num_str.zfill(9)
    red_value = int(num_str[0:3])
    green_value = int(num_str[3:6])
    blue_value = int(num_str[6:9])
    return red_value == green_value == blue_value

def testIsGray():
    print('Testing isGray()...', end='')
    assert(isGray(112112112) == True)
    assert(isGray(112112113) == False)
    assert(isGray(123195060) == False)
    assert(isGray(255255255) == True)
    assert(isGray(0) == True)
    assert(isGray(19019019) == True)
    assert(isGray(175112) == False)
    print('Passed!')

def main():
    testIsGray()

main()