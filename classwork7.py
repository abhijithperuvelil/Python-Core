# # 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# print((list(map(lambda x:x.capitalize(),names))))
# # 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# print(list(map(lambda x:x+('@gamil.com'),users)))
# # 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# print(list(filter(lambda x:x!=' ',words)))
#  # 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(list(filter(lambda x:x[0]=='A',names)))
# # 5.Concatenate all strings in a list
from functools import reduce
words = ['Python', 'is', 'fun']
print(reduce(lambda x, y: x + " "+y, words))
 # 6.Multiply all numbers in a list
# nums = [2, 3, 4]
# import functools
# print(functools.reduce(lambda x, y: x * y, nums, 1))
# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
# print(list(map(lambda x:x[0],words)))
# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,nums)))
# 9.Given a list
from hmac import new

l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
    # #Sum of Positive Odd numbers
    # #Sum of Negative  odd numbers
    # #Sum of Negative Even numbers
    # #Count of Positive numbers
    # #Count of negative numbers
even=(list(filter(lambda x:x>0 and x%2==0,l)))
print(even)
import functools
# print(functools.reduce(lambda x,y:x+y,even))
odd=(list(filter(lambda x:x>0 and x%2!=0,l)))
# print(odd)
# print(functools.reduce(lambda x,y:x+y,odd))
# negodd=list((filter(lambda x:x<0 and x%2!=0,l)))
# print(negodd)
# negeven=list((filter(lambda x:x<0 and x%2==0,l)))
# print(negeven)
# print(functools.reduce(lambda x,y:x+y,negeven))
cp=(list(filter(lambda x:x>0,l)))
print(len(cp))
cn=(list(filter(lambda x:x<0,l)))
print(len(cn))
# 10.Given a list nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
nums = ["1", "2", "3", "4"]
print(list(map(lambda x:int(x),nums)))
# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
#print products with price greater than 10000
#Find the total price of all products
p = [{'name':'laptop','price':50000},
     {'name':'phone','price':20000},
     {'name':'watch','price':3000},
     {'name':'Tablet','price':25000}]

# Product names in uppercase
print(list(map(lambda x: x['name'].upper(), p)))
print(list(filter(lambda x: x['price'] > 10000, p)))
from functools import reduce
print(reduce(lambda x, y: x + y['price'], p, 0))
