
'''
def function01():
  print("I am in function01")

function01()
'''

'''
def function01(name,age):
  print(f"I am in function01. Name is {name}, age is {age}")

function01('TechSnippets',26)
'''

# Parameters or Arguments ?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

'''
# default value arguments - default parameter should be the last parameter in function
def function01(name,age=20):
  print(f"I am in function01. Name is {name}, age is {age}")

function01('TechSnippets',26)
function01('TechSnippets')
'''


# Keyword Arguments
'''
def function01(name,age,location):
  print(f"I am in function01. Name is {name}, age is {age}, location is {location}")

# function01('TechSnippets',26,'Channai')
function01(location='Channai',name='TechSnippets',age=26)
'''

# Arbitrary arguments - accepts as tuples
'''
def function01(*courses):
  print(f"I am in function01. Courses are {courses}")
  print(f"I am in function01. course 1 is {courses[1]}")

function01('python','java')
# function01('python','java','rdbms')
'''

# Arbitrary Keyword Arguments, **kwargs - accepts as dictionary
'''
def function01(**courses):
  print(f"I am in function01. Courses are {courses}")
  print(f"I am in function01. Course 1 is {courses['course1']}")

function01(course1='python',course2='java')
'''




