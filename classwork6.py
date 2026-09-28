# # # Q1.Define a function that takes 2 numbers and returns their product
# def add(n1,n2):
#     p=n1*n2
#     return p
# n1=int(input('Enter an Number: '))
# n2=int(input('Enter another Number: '))
# a=add(n1,n2)
# print(a)
# # Q2.Define a function that takes a string and returns number of vowels
# def vowel(a):
#     count=0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count=count+1
#             return count
# n=input("Enter the String: ")
# v=vowel(n)
# print(v)
# Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     a=l*b
#     return a
# l=int(input('Enter the Length: '))
# b=int(input('Enter the Width: '))
# result=area(l,b)
# print(result)
# Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# def even(l):
#     new = []
#     for i in l:
#         if i % 2 == 0:
#             new.append(i)
#     return new
# l = [45, 78, 90, 12, 35]
# a = even(l)
# print(a)
#Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def number(l):
#     new = []
#     for i in l:
#         s = str(i)
#         total = 0
#         for j in s:
#             total = total + int(j)
#         new.append(total)
#     return new
# l = [123, 345, 111, 678, 134, 809]
# a = number(l)
# print(a)
#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
# def unique(l):
#     new = []
#     for i in l:
# #      if i in l:
#         if i not in new:
#             new.append(i)
#     return new
# l = l=[12,34,78,12,67,34,90,23]
# a = unique(l)
# print(a)
#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def duplicate(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# a=duplicate(list1,list2)
# print(a)
