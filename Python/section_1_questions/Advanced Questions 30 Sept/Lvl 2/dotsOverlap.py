def dotsOverlap(x1, y1, r1, x2, y2, r2):
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    radius_sum = r1 + r2
    return distance_squared <= radius_sum ** 2

def testDotsOverlap():
    print('Testing dotsOverlap()...', end='')
    assert(dotsOverlap(0, 0, 2, 3, 0, 2) == True)
    assert(dotsOverlap(0, 0, 2, 5, 0, 2) == False)
    assert(dotsOverlap(0, 0, 2, 4, 0, 2) == True)
    assert(dotsOverlap(-4, 5, 2, -3, 5, 5) == True)
    assert(dotsOverlap(3, 3, 3, 3, -3, 2.99) == False)
    assert(dotsOverlap(3, 3, 3, 3, -3, 3) == True)
    assert(dotsOverlap(5, 3, 0, 5, 3, 0) == True)
    print('Passed!')

def main():
    testDotsOverlap()

main()