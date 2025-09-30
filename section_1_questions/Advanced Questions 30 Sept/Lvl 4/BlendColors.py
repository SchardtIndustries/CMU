import math
def blendColors(rgb1, rgb2):
    if rgb1 < 0 or rgb1 > 255255255:
        return False
    num_str1 = str(rgb1)
    if len(num_str1) < 9:
        num_str1 = num_str1.zfill(9)
    red_value1 = int(num_str1[0:3])
    green_value1 = int(num_str1[3:6])
    blue_value1 = int(num_str1[6:9])

    if rgb2 < 0 or rgb2 > 255255255:
        return False
    num_str2 = str(rgb2)
    if len(num_str2) < 9:
        num_str2 = num_str2.zfill(9)
    red_value2 = int(num_str2[0:3])
    green_value2 = int(num_str2[3:6])
    blue_value2 = int(num_str2[6:9])
    
    red_blend = round((red_value1 + red_value2) / 2)
    green_blend = round((green_value1 + green_value2) / 2)
    blue_blend = round((blue_value1 + blue_value2) / 2)
    blended_value = red_blend * 1000000 + green_blend * 1000 + blue_blend

    return blended_value

def testBlendColors():
    print('Testing blendColors()...', end='')
    assert(blendColors(204153050, 104000152) == 154076101)
    assert(blendColors(220153102, 151189051) == 186171076)
    assert(blendColors(153051153, 51204) == 76051178)
    assert(blendColors(123456789, 123456789) == 123456789)
    assert(blendColors(0, 0) == 0)
    print('Passed!')

def main():
    testBlendColors()

main()