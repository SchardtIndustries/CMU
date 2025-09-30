def almostEqual(x, y):
    return (abs(x - y) < 10**-9)


def nthFibonacciNumber(n):
    if n == 0 or n == 1:
        return 1
    else:
        return nthFibonacciNumber(n - 1) + nthFibonacciNumber(n - 2)

def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()...', end='')
    assert(almostEqual(nthFibonacciNumber(0), 1))
    assert(almostEqual(nthFibonacciNumber(1), 1))
    assert(almostEqual(nthFibonacciNumber(2), 2))
    assert(almostEqual(nthFibonacciNumber(3), 3))
    assert(almostEqual(nthFibonacciNumber(4), 5))
    assert(almostEqual(nthFibonacciNumber(5), 8))

    print('Passed!')

def main():
    testNthFibonacciNumber()

main()