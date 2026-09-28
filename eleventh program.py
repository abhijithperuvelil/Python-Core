#write a program to check whether is armstrong
# n=int(input('Enter an Number: '))
# s=str(n)
# sum=0
# l=len(s)
# for i in s:
#     sum=sum+int(i)**l
# if sum==n:
#     print('Armstrong')
# else:
#     print('Not Armstrong')
#factors of a  number
# n=int(input('Enter Number: '))
# for i in range(1,n+1):
#     if (n%i==0):
#         print(i)
# for i in range(1,6):
#     print(i)
# else:
#     print('Hello') #it works only after the execution of the loop
# # if condition breaks before exiting loop
# for i in range(1,6):
#     if i%3==0:
#         break
#     print(i)
# else:
#     print('Hello')
# check whether a number prime or not
# n=int(input('Enter an Number: '))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print('Not Prime')
#             break
#     else:
#         print('Prime')
# else:
#     print('Number neither Prime or Composite')
# nested loop
# l=[10,20,30]
# for i in l:
#     for j in range(1,5):
#      print(i,end=" ")
#     print()
# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
# print("*")
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end=" ")
    # print()
# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)
# given a list:
from logging import raiseExceptions
from venv import create

# name=['kelly','alan','jenny']
#print kelly kelly kelly
#print alan alan alan
#print jenny jenny jenny1
# given a list
# n=[1,2,3]
# q=['what','when','why']
# print 1
# what when why
# 2
# what when why
# 3
# what when why
# #3
# given a list
# d=[{'id:101','name':'arun','age':23}]
# print each student details
# id name age
# n=['kelly','alan','jenny']
# for i in n:
#     for j in range(1,4):
#      print(i,end=" ")
#     print()
# n=[1,2,3]
# q=['what','when','why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=' ')
#     print()
# d = [
#     {'id': 101, 'name': 'arun', 'age': 23},
#     {'id': 102, 'name': 'amal', 'age': 24},
#     {'id': 103, 'name': 'anu', 'age': 25}
# ]
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()
# for i in range(1,8,2):
#    for j in range(1,i+1):
#        print('*',end=" ")
#    print()
# for i in range(1,5):
#     for j in range(1,i+1):
#        print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,i+1):
#        print(j,end=" ")
#     print()
# for i in range(4,0,-1):
#    for j in range(1,i+1):
#        print('*',end=" ")
#    print()

# given a list
# l=[23,45,78,90,12,13,91]
#print all even numbers
#print all prime numbers
# l=[23,45,78,90,12,13,91]
# for i in l:
#   for j in range(2,i):
#     if i%j==0:
#         break
#   else:
#    print(i)
# for i in l:
#     if i%2==0:
#         print(i)
# find all prime numbers in the range (1,100)
# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
# find all armstrong numbers in the rage(100,1000)
# for i in range(1,1001):
#     sum=0
#     l = len(str(i))
#     for j in str(i):
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)
# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()

# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#      print(chr(k),end=" ")
#      k = k + 1
#     print()
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#           print(0,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#           print(1,end=" ")
#     print()
# k=0
# for i in range(0,6):
#     for j in range(0,i+1):
#         # if j%2==0:
#         print(j,end=" ")
#     print()
# s='hello'
# for i in range(5):
#     for j in range(i+1):
#         print(s[j],end=" ")
#     print()
# s='hello world'
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j],end=" ") #for the value for adding in each coloumn
#     print()
# k = 6
#
#
# for i in range(1, 5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j, end="   ")
#     k -= 2
#     print()
#
# k = 2
#
# for i in range(3, 0, -1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j, end="   ")
#     k += 2
#     print()
# l=[1,2,3,4]
# new=[]
# new=[i**2 for i in l]
# print(new)
# new=[i**3 for i in new]
# print(new)
# l=[23,56,34,12,89,90,24]
# #create a new list with even values
# # create a new list with numbers greater than 50
# new=[]
# new=[i for i in l if i%2==0] # here the value of i is stored in i
# print(new)
# new=[i for i in l if i>50]
# print(new)
