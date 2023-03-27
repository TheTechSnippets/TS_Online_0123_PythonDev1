# fruits = ['apple','orange','banana','papaya','pineapple']

'''
new_fruits=[]
for fruit in fruits:
    new_fruits.append(fruit)
'''

# new_fruits=[fruit for fruit in fruits]
# print(new_fruits)

'''
for x in fruits:
    if x.startswith("a"):
        new_fruits.append(x)

print(new_fruits)
'''
# new_fruits=[a for a in fruits if a.startswith("a")]
# print(new_fruits)

#------------------------------------

base_fruits = ['apple','orange','banana','papaya','pineapple']

fruits_basket=[]

i=0
while i<10000000:
    for x in base_fruits:
      fruits_basket.append(x)
    i+=1

print(len(fruits_basket))

import datetime as dt
current_time = dt.datetime.now()

'''
new_fruits_basket_by_iter =[]
for x in fruits_basket:
    if x.startswith('a'):
     new_fruits_basket_by_iter.append(x)
'''
new_fruits_basket_by_iter=[x for x in fruits_basket if x.startswith('a')]
print("size of new_fruits_basket_by_iter : ",len(new_fruits_basket_by_iter))
end_time = dt.datetime.now()
print('Start time : ',current_time)
print('End time : ',end_time)

