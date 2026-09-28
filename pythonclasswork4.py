# # check whether the entered number is positive even or positive odd or negative even or negative odd
# n=int(input('Enter a Number: '))
# if n>0:
#     print('The Number is Positive')
#     if n%2==0:
#         print('The Number is Even')
#     else:
#         print('The Number is Not Even')
# else:
#     print('The Number is Not Positive')
# if n<0:
#     print('The Number is Negative')
#     if n%2==0:
#         print('The Number is Odd')
#     else:
#         print('The Number is Not Odd')
# else:
#     print('The Number is Not Negative')
#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
code=int(input('Enter the Item Number 1,2,3: '))
price=int(input('Enter the Price:  '))
item1=1 # Battery Based Toys
item2=2 #Key-based Toys
item3=3 #Electrical Charging Based Toys
if code==item1:
    if price>=1000:
        bill=price-(price*0.10)
        print(f"The bill is :{bill}")
    else:
        print('No Discount')
elif code==item2:
    if price>=100:
        bill=price-(price*0.05)
        print(f"The bill is :{bill}")
    else:
        print('No Discount')
elif code==item3:
   if price>=500:
       bill=price-(price*0.10)
       print(f"The Bill is {bill}")
   else:
        print("No Discount s ")
else:
    print("Invalid")

#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

# w=float(input('Enter your Weight in KG: '))
# h=float(input('Enter your Height in M: '))
# bmi=(w/h**2)
# print(f'Your BMI is {bmi}')
# if bmi<=18.4:
#     print('You are Underweight')
# elif bmi>=18.5 and bmi<=24.9:
#     print('You are Normal')
# elif bmi>=25.0 and bmi<=39.9:
#     print('You are Overweight')
# elif bmi>=40.0:
#     print('You are Obese')
# else:
#     print('Invalid')


#3 FIZZBUZZ PRoblem
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
# n=int(input('Enter an Number: '))
# if n%3==0:
#     if n%5==0:
#        print('fizzbuzz')
#     else:
#         print('fizz')
# else:
#     if n%5==0:
#       print('buzz')
#     else:
#        print(n)






