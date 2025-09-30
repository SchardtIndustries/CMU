def almostEqual(x, y):
    return (abs(x - y) < 10**-9)


def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    side_a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    side_b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    side_c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    s = (side_a + side_b + side_c) / 2
    area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
    return area

def testTriangleAreaByCoordinates():
    print('Testing triangleAreaByCoordinates()...', end='')
    assert(almostEqual(triangleAreaByCoordinates(10, 11, 14, 11, 12, 13), 4))
    assert(isinstance(triangleAreaByCoordinates(10, 11, 14, 11, 12, 13), float))
    assert(almostEqual(triangleAreaByCoordinates(2, 4.0, 2, 7, 6.0, 7), 6))
    assert(almostEqual(triangleAreaByCoordinates(0, 0, 12.0, 0, 12, 5), 30))
    assert(almostEqual(triangleAreaByCoordinates(0, 0, 0, 1, 1, 1), 0.5))
    print('Passed!')

def main():
    testTriangleAreaByCoordinates()

main()