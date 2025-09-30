import math

def numberOfSteps(bricks):
    if bricks == 0:
        return 0
    n = int((math.sqrt(8 * bricks + 1) - 1) // 2)
    if n * (n + 1) // 2 == bricks:
        return n
    else:
        return n + 1

def testNumberOfSteps():
    print('Testing numberOfSteps()...', end='')
    assert(numberOfSteps(0) == 0)
    assert(numberOfSteps(1) == 1)
    assert(numberOfSteps(2) == 2)
    assert(numberOfSteps(3) == 2)
    assert(numberOfSteps(4) == 3)
    assert(numberOfSteps(6) == 3)
    assert(numberOfSteps(7) == 4)
    assert(numberOfSteps(10) == 4)
    assert(numberOfSteps(11) == 5)
    assert(numberOfSteps(55) == 10)
    assert(numberOfSteps(56) == 11)
    print('Passed!')

def main():
    testNumberOfSteps()

main()