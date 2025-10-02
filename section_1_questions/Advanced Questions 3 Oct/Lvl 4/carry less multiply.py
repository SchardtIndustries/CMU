"""Background: Carryless Arithmetic is basic arithmetic but with the carry from each column ignored. 
For example, using carryless multiplication, 4 * 4 = 6 but 3 * 3 still equates to 9. Below is an 
example using larger numbers.

   6 4 3
 *   5 9
         
   4 6 7
 0 0 5
         
 0 4 1 7
Notice how the carry from the previous product is not added to the current number when multiplying 
and the carry from the previous column is not added to the current column when adding up the products.

With this in mind, write the function carrylessMultiply(x, y) that takes two non-negative integers x and y 
and returns their carryless product.

Hints:

You should write carrylessAdd() from the Additional Practice Exercises first as it may be useful for this problem.
Do not solve carrylessMultiply(x, y) by simply calling carrylessAdd(x, result) a total of y times. That is 
wrong on two levels. First, it is simply too inefficient (what if we are multiplying 20-digit numbers?). Second, 
it is also wrong algorithmically. Carryless multiplication is not like normal multiplication, and if we take + to be 
carrylessAdd and * to be carrylessMultiply, then it is not necessarily true that (x * y) is the same as (x + x + ... + x + x) 
for a total of y times. Yikes. So, stick with the next hint (see below). It also uses carrylessAdd() and is fairly straightforward, 
but it is reasonable efficient and algorithmically correct.
Here's a hint on one way to solve this problem. There are many ways, and this way is not the most efficient. However, it is 
efficient enough and it is perhaps among the clearest and easiest ways.
Consider multiplying 123 * 456. Observe that:

123 * 456 = (123 * 4 * 100) + (123 * 5 * 10) + (123 * 6)

In this way, we actually only have to multiply 123 times a single digit each time, then multiply that result by the right 
power of 10. Right?

So now, to multiply by a single digit, we can instead just add that many times. That is:

123 * 6 == 123 + 123 + 123 + 123 + 123 + 123

Why is that interesting? Because we already have carrylessAdd(), so we can just use that to do all this addition.

Of course, multiplying by simply adding is very inefficient. But since we are only doing it for multiplying by a 
single digit, there's a max of eight additions, and so it's not so inefficient."""

import math

def carrylessMultiply(x, y):
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

    result = 0
    place = 1
    while y > 0:
        digit_y = y % 10
        partial_product = 0
        for _ in range(digit_y):
            partial_product = carrylessAdd(partial_product, x)
        result = carrylessAdd(result, partial_product * place)
        y //= 10
        place *= 10
    return result

def testCarrylessMultiply():
    print('Testing carrylessMultiply()...', end='')
    assert(carrylessMultiply(3, 3) == 9)
    assert(carrylessMultiply(4, 4) == 6)
    assert(carrylessMultiply(12345, 0) == 0)
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)

    print('Passed!')

def main():
    testCarrylessMultiply()

main()