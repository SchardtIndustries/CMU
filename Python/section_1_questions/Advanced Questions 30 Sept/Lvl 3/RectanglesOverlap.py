def rectanglesOverlap(left1, top1, width1, height1,
                      left2, top2, width2, height2):
    right1 = left1 + width1
    bottom1 = top1 - height1
    right2 = left2 + width2
    bottom2 = top2 - height2
    return (left1 <= right2 and right1 >= left2 and bottom1 <= top2 and top1 >= bottom2)


def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    # Intersect at right of rectangle 1
    assert(rectanglesOverlap(1,1,5,1,6,1,2,2) == True)
    # Intersect at top of rectangle 1
    assert(rectanglesOverlap(1,4,5,3,1,5,8,3) == True)
    # Intersect at left of rectangle 1
    assert(rectanglesOverlap(1,5,6,6,-4,7,5,3) == True)
    # Intersect at bottom of rectangle 1
    assert(rectanglesOverlap(10,10,3,3,9,7,3,3) == True)
    # Partially overlapping rectangles
    assert(rectanglesOverlap(1,7,3,6,3,4,2,5) == True)
    # Don't intersect
    assert(rectanglesOverlap(1,4,3,3,10,10,5,5) == False)
    # Don't intersect, but x-coordinates overlap
    assert(rectanglesOverlap(1,4,30,3,10,10,5,5) == False)
    # Don't intersect, but y-coordinates overlap
    assert(rectanglesOverlap(1,4,3,15,10,10,5,5) == False)
    print('Passed!')

def main():
    testRectanglesOverlap()

if __name__ == "__main__":
    main()
