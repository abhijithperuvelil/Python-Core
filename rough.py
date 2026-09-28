# student_grades={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}
# print(student_grades['Charlie'])
# print(student_grades.keys())
# print(student_grades.items())
# print(student_grades.values())
# Write a program to:
#
# If the balance is greater than or equal to the withdrawal amount:
# If the withdrawal amount is a multiple of 100, print "Transaction Successful".
# Otherwise, print "Enter amount in multiples of 100".
# Otherwise, print "Insufficient Balance".
# a=int(input('Enter the Amount: '))
# balance=5000
# if a<=balance:
#     if a%100==0:
#         print('Transaction Successful')
#     else:
#          print('The Amount Must Be Multiple of 100')
# else:
#     print('Insufficient Balance')

# Question: Movie Ticket Booking 🎬
#
# Write a program to:
#
# Ticket price = ₹200
# Ask the user for their age and money.
# If the user has at least ₹200:
# If the age is 18 or above, print "Ticket Booked".
# Otherwise, print "Not Eligible (Must be 18+)".
# Otherwise, print "Insufficient Money".

# a=int(input('Enter Your Age: '))
# amount=int(input('Enter Your Amount: '))
# Price=200
# if a>=18:
#     if amount>=200:
#         print('Tickets Booked')
#     else:
#         print('Insufficient Amount')
# else:
#     print('Not Eligible (Must be 18+)')
# Write a program to:
#
# Password = 1234
    # Ask the user to enter a password and an OTP.
    # If the password is correct:
    # If the OTP is 5678, print "Login Successful".
    # Otherwise, print "Invalid OTP".
    # Otherwise, print "Incorrect Password".

# p=int(input('Enter the Password: '))
# o=int(input('Enter the otp: '))
# password=1234
# otp=5678
# if p==password:
#     if o==otp:
#         print("Login Successful")
#     else:
#         print('Invalid Otp')
# else:
#     print("Wrong Password")

# ATM Withdrawal Problem
# Ask the user to enter the ATM PIN and withdrawal amount
# If the PIN is correct (4321)
#     If the withdrawal amount is less than or equal to the balance (10000)
#         If the amount is a multiple of 100
#             Print "Transaction Successful"
#         Otherwise
#             Print "Enter amount in multiples of 100"
#     Otherwise
#         Print "Insufficient Balance"
# Otherwise
#     Print "Invalid PIN"

# Write a Python program that:
#
# Ask the user to enter their username.
# If the username is student123:
# Ask the user to enter the password.
# If the password is python@123:
# Print "Login Successful. Exam Started."
# Otherwise:
# Print "Incorrect Password."
# Otherwise:
# Print "Username Not Found."

# user=input('Enter username: ')
# p=input('Enter password: ')
# if user=='student123':
#     if p=='python@123':
#        print('Login Successful')
#     else:
#         print('Wrong Password')
# else:
#     print('Wrong Username')
# Print all numbers between 1 and 100 that contain the digit '7'.
# i=1
# while(i<=100):
#     s=str(i)
#     if s[-1]=="7":
#       print(i)
#     i=i+1
# product of first 10 even numbers
# i=2
# product=1
# while(i<=10):
#     if i%2==0:
#         #print(i)
#         product=product*i
#     i=i+1
# print(product)
#multiplication table of a number upto 10
# n=int(input('Enter an Number: '))
# i=1
# while i<=10:
#     print(i,'*',n,'=', i*n)
#     i=i+1
#print those numbers are divisible by 5
# #print those numbers which contains 3
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%5==0:
#         print(i)
#
# # l=[12,34,56,45,89,16,69,33]
# for i in l:
#     i=str(i)
#     if '3' in i:
#         print(i)
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     i=str(i)
#     if '4' in i:
#         print(i)
# Question: Print all numbers that:
#
# Contain the digit '3'.
# Are divisible by 5
# l = [10, 23, 35, 42, 53, 64, 73, 81, 93, 100]
# # for i in l:
# #     i=str(i)
# #     if '3' in i:
# #         print(i)
# # for i in l:
# #     if i%5==0:
# #         print(i)
# l = [10, 23, 35, 42, 53, 64, 73, 81, 93, 100]
# i=l[0:1]
# print(i)
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
# for i in range(1,100):
#     if i%3==0:
#         if i%5==0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#         if i%5==0:
#             print('Buzz')
#     else:
#         print(i)
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
# #     sum of digits in  a number
# n=int(input('Enter an Number: '))
# r=''
# count=0
# sum=0
# for i in str(n):
#     r=i+r
# print(r)
# for i in str(n):
#     count=count+1
# print(count)
# for i in str(n):
#     sum=sum+int(i)
# # print(sum)
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
# n=int(input('Enter an Number: '))
# sum=0
# s=str(n)
# l=len(s)
# for i in s:
#    sum=sum+int(i)**l
# if sum==n:
#     print('Armstrong')
# else:
#        print('Not Armstrong')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
