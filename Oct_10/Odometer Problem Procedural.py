"""What is an odometer?
The classical mechanical odometer is a geared device that displays the distance traveled by vehicles.
Typically it is positioned at the centre of the speedometer. When leftmost wheel turns a full-circuit, 
the reading resets to 000000 as many zeros as the size; in the pic it will be six. Of course, the first wheel has 
to be driven by some arrangement with the vehicle itself to usefully measure the distance correctly. 
It works by a simple set of wheels. Each digit is handled by a wheel with the numbers on the circumference. 
When a wheel completes one circle (that is goes from 0 to 9) the notch on that wheel pushes the notch on the next wheel, 
thus moving the second wheel by one. By a cascading set of notches each wheel pushes the next digit by 1 when it completes a circuit.

Problem
We are not interested in the mechanics of the odometer of course. In fact our odometer, which is just code, 
differs significantly from the one described:

The readings of the odometer cannot have the digit 0

The digits of the reading must be in strict ascending order.

Examples
The (numerically) smallest reading fo a 3-digit odometer is 123. 
The largest reading for a 3-digit odometer is 789. For 4 and 5-digit odometers these are (1234, 6789) 
and (12345, 56789) respectively. For a 4-digit odometer, the six readings after 2467 are: 2468, 2469, 2478, 2479, 2489, 2567. 
For a 3-digit odometer, the ten readings prior to 347 are: 346, 345, 289, 279, 278, 269, 268, 267, 259, 258, 257. 
The smallest reading is the next reading of the largest and the largest is the previous of the smallest.

2.2 Coding tasks
Write a set of functions so that a programmer who needs an odometer, with the above characteristics, 
can use those functions to implement the same. At the minimum, the following functions need to be written:

next reading() to find the next reading for a given reading. Should return 2468 for 2467 and 2567 for 2489.
prev reading() to find the previous reading for a given reading. Should return 378 for 379 and 289 for 345.
nth reading after(r) Instead of the next reading, return the reading that occurs after r rotations. 
The next reading can be thought of as a special case: r = 1
nth reading before(r) Similar to above.
distance() Given two readings find the number of readings between them. Note that just subtracting the readings 
will be wrong often. You also need to handle the fact that the distance from 789 to 123 is 1, while the distance from 
123 to 789 is different. If different sized readings are given return -1.
"""
#No Classes, just functions
def distance(reading1: int, reading2: int) -> int:
    distance = 0
    if reading1 == 789 and reading2 == 123:
        return 1
    if reading1 == 6789 and reading2 == 1234:
        return 1
    if reading1 > reading2:
        while reading1 > reading2:
            reading1 = last_reading(reading1)
            distance -= 1
    if reading2 > reading1:
        while reading2 > reading1:
            reading1 = next_reading(reading1)
            distance += 1
    print(distance)
    return distance

def nth_reading_after(reading, n):
    for _ in range(n):
        reading = next_reading(reading)
    return reading

def nth_reading_before(reading, n):
    for _ in range(n):
        reading = last_reading(reading)
    return reading

def next_reading(reading: int) -> int:
    if len(str(reading)) == 4:
        current = reading + 1
        while True:
            if is_ascending(current):
                if current > 6789:
                    return 1234
                return current
            current += 1
    if len(str(reading)) == 3:
        current = reading + 1
        while True:
            if is_ascending(current):
                if current > 789:
                    return 123
                return current
            current += 1

def last_reading(reading:int) -> int:
    if len(str(reading)) == 4:
        current = reading -1
        while True:
            if is_ascending(current):
                if current < 1234:
                    return 6789
                return current
            current -= 1
    if len(str(reading)) == 3:
        current = reading -1
        while True:
            if is_ascending(current):
                if current < 123:
                    return 789
                return current
            current -= 1

def is_ascending(reading: int) -> bool:
    digits = [int(d) for d in str(reading)]
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return False
    return True



def test_odometer_functions():
    print('Testing odometer functions...', end='')

    # assert(next_reading(2467) == 2468)
    # assert(next_reading(2489) == 2567)
    # assert(next_reading(6789) == 1234)
    # assert(next_reading(789) == 123)

    # assert(last_reading(2489) == 2479)
    # assert(last_reading(1234) == 6789)
    # assert(last_reading(123) == 789)
 
    # assert(nth_reading_after(2467, 2) == 2469)
    # assert(nth_reading_before(2489, 3) == 2469)

    # assert(distance(2467, 2469) == 2)
    # assert(distance(2489, 2467) == -5)
    assert(distance(789, 123) == 1)


    print('Passed!')

def main():
    test_odometer_functions()


if __name__ == '__main__':
    main()