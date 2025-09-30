import math

def howManyPizzas(students: int, slices_per_student: int) -> int:
    total_slices = students * slices_per_student
    slices_per_pizza = 8
    numPizzas = math.ceil(total_slices / slices_per_pizza)
    return numPizzas

def testHowManyPizzas():
    print('Testing howManyPizzas()...', end='')
    assert(howManyPizzas(8, 1) == 1)
    assert(howManyPizzas(9, 1) == 2)
    assert(howManyPizzas(5, 4) == 3)
    assert(howManyPizzas(10, 2) == 3)
    assert(howManyPizzas(0, 0) == 0)
    assert(howManyPizzas(0, 3) == 0)
    assert(howManyPizzas(10, 0) == 0)
    assert(howManyPizzas(3, 4) == 2)
    print('Passed!')

def main():
    testHowManyPizzas()

main()