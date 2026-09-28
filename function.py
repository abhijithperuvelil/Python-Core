# def add():
#     n1=int(input('Enter an Number: '))
#     n2=int(input('Enter an Number: '))
#     sum=n1+n2
#     print("Sum of the Numbers",sum)
#     return
# add()
#define a function to display "hello your Name"
# def disp():
#     name=input('Enter Your Name: ')
#     print("Hello ",name)
#     return
# disp()
#define a Function to find the factorial of a number
# def fact():
#     fact = 1
#     n=int(input("Enter an Number: "))
#     for i in range(1, n + 1):
#      fact = fact * i
#     print(fact)
#     return
# fact()
#define a function to find the count of a specific character in a give string
# def count_ch():
#     count=0
#     s=input('Enter a word: ')
#     ch=input('Enter a string')
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# count_ch()
#define a function to check whether a number is prime or not
# def prime():
#     n=int(input('Enter an Number: '))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print('Not Prime')
#                 break
#         else:
#             print('Prime')
#     else:
#         print('Neither Prime Or Zero')
#     return
# prime()
#define a function to find the factors of a numbers
# def factor():
#     n=int(input('Enter an Number: '))
#     for i in  range(1,n+1):
#         if n%i==0:
#             print(i)
#     return # exit
# factor()
# def add(s1,s2):
#     s=a+b
#     print(s)
# # add(23,23)
# a=int (input('Enter an Number: '))
# b=int(input('Enter another Number: '))
# add(a,b)
#define a function that take 3 arguments amount,years and rate as arguments and find the simple interest
# def interest(p,n,r):
#     si=(p*n*r)/100
#     print("Simple Interest",si)
# p=int(input("Enter the Amount: "))
# n=int(input("Enter the Year: "))
# r=int(input("Enter the Rate: "))
# interest(p,n,r)
#define a function that takes 2 numbers as arguments and return sum as result call the function and print the result
# def add(n1,n2):
#     s=n1+n2
#     return s
# a=add(23,56)
# print(a)
# def add(n1,n2):
#     s=n1+n2
#     return s
# n1=int(input('Enter an Number: '))
# n2=int(input('Enter another Number: '))
# a=add(n1,n2)
# print(a)
#define a function that takes a string as argument and returs a new dictionary where keys are words values are length of each word
#call the function and print the dictionary
# s='python coding is easy and fun'
# def dict(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     # new={i:len(i) for i in s.split()} # comprehension
#     return new
# a=dict(s)
# print(a)
#define a function that takes a number as argument and check whether that number is spy number or not
# def spy(n1):
#     sum=0
#     product=1
#     for i in str(n1):
#         sum=sum+int(i)
#         product=product*int(i)
#     if sum==product:
#         result='Spy Number'
#     else:
#         result='Not Spy'
#     return result
# n1=int(input("Enter an Number: "))
# a=spy(n1)
# print(a)
