# Python Recursive Function
'''
Generally A function can call other functions.
It is even possible for the function to call itself. These are termed as recursive functions.
'''

'''
def recursive_function(value):
    print(f'I am in recursive function : {value}')
    recursive_function(value+1)
    
recursive_function(1)
'''


# RecursionError: maximum recursion depth exceeded while calling a Python object
'''
import sys
sys.setrecursionlimit(6)
print(sys.getrecursionlimit())

def recursive_function(value):
    print(f'I am in recursive function : {value}')
    recursive_function(value+1)
    
recursive_function(1)
'''

# Factorial of number
# Lets say x = 5 : Then  x factorial, x! is 5 * 4 * 3 * 2 * 1


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("The factorial of", num, "is", factorial(num))


# print all even numbers from 1 to 1000
initial=0
last = 1000

def function01(initial):
    print(f"value is : {initial}")
    if(initial == 1000):
        return 0
    function01(initial+2)

function01(0)
