# for i in range(1,101):
#     if i%2==0 and i%3==0:
#         print(i)
# l=[1, 2, 3, 4]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
# l = [10, 20, 30, 40, 50]
# sum=0
# for i in range(0,len(l),2):
#     sum+=l[i]
# print(sum)
# 5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# l=[4,9,1,0,6,7]
# sum=0
# for i in l:
#     sum+=i
#     if i==0:
#         break
# print(sum)
# Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1,1001):
#     if i%7==0 and i%11==0:
#         print(i)
#         break
# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# l=['name','place','profession','english','color']
# for i in l:
#     if len(i)>5:
#         print(i)
#         continue
# 8.From a list of numbers, create a new list containing the squares of each element.
# l = [1, 2, 3]
# new=[]
# for i in l:
#     new=i**2
#     print(new)
# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# a=input("Enter an String: ")
# for i in a:
#     if i not in 'aeiouAEIOU':
#         print(i)
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l=[5,2,8,6,2,30]
# new=[]
# for i in l:
#     x=i*2
#     if x>50:
#         break
#     new.append(x)
# print(new)
#  11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
# n=input("Enter the Chara: ")
# for i in n:
#     if i>'0' and i<'9':
#         print(i)
#  12.Given a list of strings, create a new list containing the length of each string.
# l=['cat','banana','']
# new=[]
# for i in l:
#     new=print(len(i))
# 13.Given a list of words, create a string made of the first letter of each word.
# l=["Python", "Is", "Great"]
# s=""
# for i in l:
#     s=(i[0])
#     print(s)
# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# l=[4, -3, 2, -1]
# new=[]
# for i in l:
#     if i<0:
#         i=0
#     new.append(i)
# print(new)
# 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# # #print all names of students
# for i in d.values():
#     print(i[0])
# 16.Write a program to print the numbers from 1 to 100.
# But for multiples of:
#
# 3, print “Fizz” instead of the number
#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# Otherwise, print the number itself
# for i in range(1,101):
#     if i%3==0:
#         if i%5==0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     else:
#         if i%5==0:
#             print("Buzz")
#         else:
#             print(i)
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break
# for i in range(1,51):
#     # if i%5==0:
#     #     continue
#     # print(i)
#     if i>40:
#         break
#     print(i)
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number
from heapq import nlargest
from itertools import count
from token import GREATER
from zipimport import END_CENTRAL_DIR_LOCATOR_SIZE_64

import reduce

# n=int(input("Enter an Number: "))
# r=''
# sum=0
# count=0
# for i in str(n):
# #     r=i+r
# # print(r)
# #     count=count+1
# # print(count)
#     sum=sum+int(i)
# print(sum)
# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(n1,n2):
#     product=n1*n2
#     return product
# n1=int(input("Enter an Number: "))
# n2=int(input("Enter an Number: "))
# a=product(n1, n2)
# print(a)
# Q2.Define a function that takes a string and returns number of vowels
# def vowel(a):
#     count=0
#     for i in a:
#         if i in 'aeiouAEIOU':
#          count=count+1
#     return count
# n=input('Enter the String: ')
# v=vowel(n)
# print(v)
# Write a Python function that takes a string as an argument and returns the number of consonants in the string.
# def consonants(n):
#     count=0
#     for i in n:
#         if i not in "AEIOUaeiou":
#            count=count+1
#     return count
# n=input("Enter the word: ")
# a=consonants(n)
# print(a)
# Write a Python function that takes a string as an argument and returns the number of digits present in the string.
# def digits(n):
#     count=0
#     for i in n:
#         if i>='0' and i<='9':
#             count=count+1
#     return count
# n=input("Enter the Words: ")
# a=digits(n)
# print(a)
# Input:  "python is very easy"
# Output: 3
# def space(n):
#     count=0
#     for i in n:
#         if i==" ":
#             count=count+1
#     return count
# n=input("Enter the Word: ")
# a=space(n)
# print(a)
# Write a Python function that takes a string as an argument and returns the number of characters that are equal to 'a'.
# def chara(c):
#     count=0
#     for i in c:
#         if i=='n':
#             count=count+1
#     return count
# c=input('Enter the Word: ')
# a=chara(c)
# print(a)
# Write a Python function that takes a string as an argument and returns the number of characters that are not vowels.
# def chara(n):
#     count=0
#     for i in n:
#         if i not in 'aeiouAEIOU':
#             count=count+1
#     return count
# n=input("Enter the Word: ")
# a=chara(n)
# print(a)
# factorial
# def fact(n1):
#     x=1
#     for i in range(1,n1+1):
#         x=x*i
#     return x
# n1=int(input("enter a Number: "))
# a=fact(n1)
# print(a)
# prime
# def prime(n1):
#     a="prime"
#     b="not prime"
#     for i in range(2,n1):
#         if n1%i==0:
#             return b
#     else:
#         return a
# n1=int(input("enter an Number: "))
# x=prime(n1)
# print(x)
# # factors of a number
# def factors(n1):
#     for i in range(1,n1+1):
#         if n1%i==0:
#             print(i)
# n1=int(input("enter an Number: "))
# x=factors(n1)
# print(x)
# armstrong
# def armstrong(n1):
#     s=str(n1)
#     sum=0
#     a="armstrong"
#     b = "not armstrong"
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n1:
#         return a
#     else:
#         return b
# n1=int(input("Enter an Number: "))
# a=armstrong(n1)
# print(a)
# Define a function that takes a number as an argument and checks whether it is a palindrome.
# def pal(n1):
#     a='yes'
#     b='no'
#     n=str(n1)
#     if n==n[::-1]:
#         return a
#     else:
#         return b
# n1=int(input("Enter an Number: "))
# a=pal(n1)
# print(a)
#  Define a function that takes a number as an argument and returns the reversed number.
# def rev(n1):
#     n=str(n1)
#     a=n[::-1]
#     return a
# n1=int(input("Enter an Number: "))
# a=rev(n1)
# print(a)
# def per(n1):
#     sum=0
#     a='yes'
#     b='no'
#     for i in range(1,n1):
#         if n1%i==0:
#             sum=sum+i
#     if sum==n1:
#         return a
#     else:
#         return b
# n1=int(input("Enter an Number: "))
# a=per(n1)
# print(a)
# Define a function that takes two numbers and returns the larger number.
# def large(n1,n2):
#     if n1>n2:
#         l=(n1 ,'is GREATER')
#         return l
#     else:
#         m=(n2 ,'is GREATER')
#         return m
# n1=int(input("Enter an Number: "))
# n2=int(input("Enter an Number: "))
# a=large(n1, n2)
# print(a)
# l1=[1,2,3,5,6]
# for i in range(1,10):
#     if i not in l1:
#         print(i)Filter all positive even numbers
# Filter all positive odd numbers
# Find the sum of all positive numbers
# Find the product of all positive even numbers
# Count how many negative numbers are present
# Add 5 to every number
# Find the square of every number
nums = [10, 15, 20, 25, 30, 35, 40, -5, -10]
# positive=list(filter(lambda x:x>0,nums))
# print(positive)
# from functools import reduce
# print(reduce(lambda x, y: x+y,positive, 0))
# peven=list(filter(lambda x:x>0 and x%2==0,nums))
# print(reduce(lambda x,y:x+y,peven,0))
# neg=list(filter(lambda x:x<0,nums))
# print(neg)
# print(len(neg))
# # print(list(map(lambda x:x+10,nums)))
# print(list(map(lambda x:x**2,nums)))