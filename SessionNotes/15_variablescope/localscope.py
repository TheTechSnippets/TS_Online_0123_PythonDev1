# A variable created inside a function is available inside that function
'''
def function01():
    var1 = 100
    print(f'var1 value is inside function {var1}')

function01()
print(f'var1 value is outside function {var1}')
'''

# function inside function - inner function
# The variable var1 is not available outside the function, but it is available for any function inside the function
'''
def function01():
    var1 = 300

    def inner_function01():
        print(f'var1 value is inside inner function - inner_function01 : {var1}')

    inner_function01()
    print(f'var1 value is inside function {var1}')

function01()
'''

# Naming variables
# If you use the same variable name inside and outside of a function,
# Python will treat them as two separate variables, one available in the global scope (outside the function)
# and one available in the local scope (inside the function)
'''
var1 = 200

def function01():
    var1 = 300

    def inner_function01():
        print(f'var1 value is inside inner function - inner_function01 : {var1}')

    inner_function01()
    print(f'var1 value is inside function {var1}')


function01()
print(f'var1 value is outside function {var1}')
'''

