"""
This is the doc outside the func
"""


def function_01():
    """this is the doc inside the function 01"""
    print("i am in function 01")


def function_02():
    print("i am in function 02")
    """this is the doc inside the function 02"""


if (__name__ == '__main__'):
    print(__doc__)
    print(function_01.__doc__)
    print(function_02.__doc__)
