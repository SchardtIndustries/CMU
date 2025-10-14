#Data Types
print(1)
print(2, 3)
print(type(42))
print(type(3.14))
print(type("Hello, World!"))
print(type("hello"))
print('4' * 10)
print(4 * 10)
print(type(True))
print(type(False))
print(type(None))

#Variables
x = 10
print(x)
y = 3.14
print(y)
name = "Alice"
print(name)
age = 25
print(age)
is_student = True
print(is_student)
height = None
print(height)
numberOfCats = 3 #Camel Case
number_of_cats = 3 #Snake Case

#F-Strings
name = "Bob"
age = 30
height = 5.9
is_student = False
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
x = 42
y = 3.14
print(f"x: {x}, y: {y}, sum: {x + y}")

#Statements
x = 10
print(x)

#Expressions
x = 10          #10 is an expression
print(x)
y = 5 + 3   #5 + 3 is an expression
print(y)
z = y * 2   #y * 2 is an expression
print(z)

#Operators
x = 12 + 5  # + is the operator
            # 12 and 5 are operands
            # 12 + 5 is the expression
print(x)

#Functions

larger_number = max(10, 20) #calls built-in function max
                            #10 and 20 are arguments
                            #larger_number is the return value
                            #the function call is an expression
print(larger_number)

def sumOfSquares(a, b):
    return a**2 + b**2

x = sumOfSquares(3, 4) #calls user-defined function sumOfSquares
                        #3 and 4 are arguments
                        #x is the return value
                        #the function call is an expression
print(x)

#modules
import math
x = math.sqrt(16) #calls sqrt function from math module
y = math.pi    #accesses pi constant from math module
print(x)
print(y)

from math import sqrt, pi
x = sqrt(25)  #calls sqrt function directly
y = pi        #accesses pi constant directly
print(x)
print(y)

#Console Input
name = input("Enter your name: ") #input function reads a line from input
age = input("Enter your age: ")   #input function reads a line from input
print(f"Hello, {name}! You are {age} years old.")

#Errors
#Syntax Error Example
# print("Hello, World!"
    
#runtime Error Example
# x = 10 / 0

#logical Error Example
#print(5 squared is 23) #should be 25

#testing and debugging

#testing involves running code with various inputs to ensure it behaves as expected
#debugging involves identifying and fixing errors in the code

#arithmetic Operators
x = 10 + 5    #Addition
y = 10 - 5    #Subtraction
z = 10 * 5    #Multiplication
a = 10 / 5    #Division
b = 10 // 3   #Floor Division
c = 10 % 3    #Modulus
d = 2 ** 3    #Exponentiation
#if either is a float the result is a float
# // and % always return an integer if both operands are integers
# // and % return a float if either operand is a float
# / always returns a float
print(18//5) #3
print(18%5)  #3
print(18/5)  #3.6
print(-18//5) #-4
print(-18%5)  #2
print(-18/5)  #-3.6
#if you divide by zero you get a runtime error
#exponentiation has higher precedence than multiplication
result = 2 + 3 * 4 ** 2 #2 + 3 * 16 = 2 + 48 = 50
print(9 ** (1/2)) #3.0
#remainder
print(21 % 6) #3
print(21 % -6) #-3
print(-21 % 6) #3
print(-21 % -6) #-3
print(21%21) #0
print(21%-21) #0
print(0%21) #0

#Assignment Operators
x = 10
x += 5  #x = x + 5
print(x) #x = 15
x -= 3  #x = x - 3
print(x) #x = 12
x *= 2  #x = x * 2
print(x) #x = 24
x /= 4  #x = x / 4
print(x) #x = 6.0
x //= 3 #x = x // 3
print(x) #x = 2.0
x %= 2  #x = x % 2
print(x) #x = 0.0
x **= 3 #x = x ** 3
print(x) #x = 0.0

#relational Operators
x = 10
y = 20



    