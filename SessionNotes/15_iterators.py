fruits = ['apple','orange','banana','papaya','pineapple']

# iterator

iterable_fruits = iter(fruits)

# print(next(iterable_fruits))

while True:
    try:
        print(next(iterable_fruits))
    except StopIteration:
        break
        
'''
name = 'TechSnippets'
for letter in name:
    print(letter)
'''

'''
items = ['apple','banana','orange']
for item in items:
    print(item)
'''

'''
name = 'TechSnippets'
iterable_name = iter(name)
# print(next(iterable_name))
# while True:
#     letter = next(iterable_name)
#     print(letter)
while True:
    try:
        letter = next(iterable_name)
        print(letter)
    except StopIteration:
        break
        
'''
