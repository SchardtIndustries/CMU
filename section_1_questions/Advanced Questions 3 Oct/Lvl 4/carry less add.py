"""Background: Carryless Arithmetic is basic arithmetic but with the carry from each column ignored. For example, 
using carryless addition, 8 + 7 = 5. Below is an example using larger numbers.

   7 8 5
 + 3 7 6
         
   0 5 1
Notice how the carry from the previous column is not added to the current column.

With this in mind, write the function carrylessAdd(x, y) which takes two non-negative integers 
x and y and returns their carryless sum.
"""

def carrylessAdd(x, y):
    result = 0
    place = 1
    
    while x > 0 or y > 0:
        digit_x = x % 10
        digit_y = y % 10
        
        carryless_digit = (digit_x + digit_y) % 10
        result += carryless_digit * place
        
        x //= 10
        y //= 10
        place *= 10
    
    return result

def testCarrylessAdd():
    print('Testing carrylessAdd()...', end='')
    assert(carrylessAdd(8, 7) == 5)
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 325) == 325)
    assert(carrylessAdd(30, 873) == 803)
    assert(carrylessAdd(873, 30) == 803)
    assert(carrylessAdd(100, 11) == 111)
    print('Passed!')

def main():
    testCarrylessAdd()

main()