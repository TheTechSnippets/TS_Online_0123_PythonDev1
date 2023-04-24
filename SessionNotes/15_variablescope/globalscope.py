# Global Keyword
# To create a global variable, from the local scope (inside function), you can use the global keyword
# The global keyword makes the variable global.
'''
def function01():
    global var1
    var1 = 100
    print(f'var1 value is inside function {var1}')

function01()
print(f'var1 value is outside function {var1}')
'''

# Use the global keyword if you want to make a change to a global variable inside a function.
'''
var1 = 200

def function01():
    global var1  # check the output by adding and removing this line
    var1 = 300

    def inner_function01():
        print(f'var1 value is inside inner function - inner_function01 : {var1}')

    inner_function01()
    print(f'var1 value is inside function {var1}')


function01()
print(f'var1 value is outside function {var1}')
'''

