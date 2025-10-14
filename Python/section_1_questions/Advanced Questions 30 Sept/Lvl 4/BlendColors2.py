def blend(c1: int, c2: int) -> int:
    return round((c1 + c2) / 2)

def blendColors(rgb1, rgb2):
    red1, red2 = (rgb1 // 1000000), (rgb2 // 1000000)
    green1, green2 = (rgb1 // 1000) % 1000, (rgb2 // 1000) % 1000
    blue1, blue2 = rgb1 % 1000, rgb2 % 1000

    blendred = blend(red1, red2)
    blendgreen = blend(green1, green2)
    blendblue = blend(blue1, blue2)

    paddedred = blendred * 1000000
    paddedgreen = blendgreen * 1000
    blended_value = paddedred + paddedgreen + blendblue
    return blended_value

def testBlendColors():
    print('Testing blendColors()...', end='')
    assert(blend(255, 200) == 228)
    assert(blendColors(204153050, 104000152) == 154076101)
    assert(blendColors(220153102, 151189051) == 186171076)
    assert(blendColors(153051153, 51204) == 76051178)
    assert(blendColors(123456789, 123456789) == 123456789)
    assert(blendColors(0, 0) == 0)
    print('Passed!')

def main():
    testBlendColors()

main()