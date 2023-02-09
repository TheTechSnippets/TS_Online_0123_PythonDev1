'''
Why it is important to handle exceptions ?
'''

'''
print("Welcome to the program..!")
a = 5
b = 0
sum = a + b
print(f'sum is {sum}')
div = a / b
print(f'div is {div}')
diff = a - b
print(f'diff is {diff}')
print("All operations are over..!")
print(" exiting the program..! Bye.!!")
'''

# Handling exceptions
'''
try, except, finally, raise - Python
try, catch,  finally, throw, throws - Java
'''

'''
try:
    print("Welcome to the program..!")
    a = 5
    b = 0
    sum = a + b
    print(f'sum is {sum}')
    div = a / b
    print(f'div is {div}')
    diff = a - b
    print(f'diff is {diff}')
    print("All operations are over..!")
except:
    print("some exception occurs..!!")

print("outside the try/exception blocks")
print("exiting the program..! Bye.!!")
'''

'''
try:
    print("Welcome to the program..!")
    items = ['a', 'b', 'c']
    print(f'printing items[0] : {items[2]}')
    div = 5 / 1
    f1 = open('f1.txt')
    print("All operations are over..!")

except IndexError:
    print("Index out of range . you are trying to access index not available")
    print(f'Available size is : {len(items)}')
except ZeroDivisionError:
    print("you are trying to divide a number by zer0.. dont do it.. have some sense")
except:
    print('some other exception happened...')

print("outside the try/exception blocks")
print("exiting the program..! Bye.!!")
'''

'''
try:
    print("Welcome to the program..!")
    items = ['a', 'b', 'c']
    print(f'printing items[0] : {items[3]}')
    div = 5 / 1
    f1 = open('f1.txt')
    print("All operations are over..!")

except IndexError as ie:
    print(repr(ie))
    print("Index out of range .")
    print(f'Available size is : {len(items)}')
except ZeroDivisionError as zde:
    print("you are trying to divide a number by zer0.. dont do it.. have some sense")
except:
    print('some other exception happened...')

print("outside the try/exception blocks")
print("exiting the program..! Bye.!!")
'''

names = ['Dharani','Priya','Hajeestha']
try:
    print("Welcome to the program..!")
    items = ['a', 'b', 'c']
    print(f'printing items[0] : {items[2]}')
    div = 5 / 1
    # f1 = open('f1.txt')
    name = input("enter user id : ")
    if name not in names:
        raise RuntimeError('name not available')
    print("All operations are over..!")
except (IndexError, ZeroDivisionError):
    print("some arithematic exception")
except RuntimeError as rte:
    print(repr(rte))
except:
    print('some other exception happened...')
finally:
    print("i am important")

print("outside the try/exception blocks")
print("exiting the program..! Bye.!!")


