#Write a program to create a list of 5 random 3 digit numbers
# import random
# new=[]
# for i in range(5):
#     x=random.randint(100,1000)
#     new.append(x)
# print(new)
#write a program to create a 5digit random otp number
# import random
# x=random.randint(10000,100000)
# print(x)
#write a program to find the position of a character in a string
s=input("Enter the String: ")
n=input("Enter The Character: ")
if s in n:
    print(s.index(n))
else:
    print('Character is Not Present')
#define a function that takes a string as argument and returns a new dictionary
#where keys are character and values are count of each character
# def dict(n):
#     new={}
#     for i in n:
#         if i in new:
#             new[i]=new[i]+1
#         else:
#             new[i]=1
#     return new
# n=input("Enter the Word: ")
# a=dict(n)
# print(a)
#Define a function that takes string as argument and print the count of
# digits,spaces,letters in that string
# def count(s):
#     digit=0
#     alpha=0
#     space=0
#     for i in s:
#         if i.isdigit():
#             digit=digit+1
#         elif i.isalpha():
#             alpha=alpha+1
#         elif i.isspace():
#             space=space+1
#     print("Number of Digits",digit)
#     print("Number of Letters",alpha)
#     print("Number of Spaces",space)
#     return
# count('hello')
