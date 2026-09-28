# #Write a program to check whether two entered numbers are equal or not
# n1=int(input('Enter a number: '))
# n2=int(input('Enter another Number: '))
# if n1==n2:
#     print('The Numbers are Equal')
# else:
#     print('The Numbers are Not Equal')
## #Write a program to check whether two entered words are equal or not
# w1=(input('Enter a Word: '))
# w2=(input('Enter another Word: '))
# if w1==w2:
#     print('The Words are Equal')
# else:
#     print('The Words are Not Equal')
#Write a program to find the maximum of two numbers
# n1=int(input('Enter a number: '))
# n2=int(input('Enter another Number: '))
# if n1>n2:
#     print('The N1 is Greater')
# else:
#     print('The N2 is Greater')
# #write a program to check whether the entered character is vowel or not
# ch=input('Enter an character: ')
# vowel="aeiouAEIOU"
# if ch in vowel:
#     print("The Character is Vowel")
# else:
#     print("The Character is Not Vowel")
#Write a program to check whether the entered country name contains word 'land'
# count=input('Enter the Country:')
# if  'land' in count:
#     print('The Country Contains Land ')
# else:
#     print('No')

#write a program to check whether the entered number is 3 digit or not
# n1=int(input('Enter a number: '))
# if n1>=100 and n1<=999:
#     print('The Number is 3 Digit')
# else:
#     print('The Number is Not 3 Digit')

#write a program to check whether the entered string is  palindromde or not
# s=input('Enter an Word: ')
# if s==s[::-1]:
#     print('The Word is palindromde')
# else:
#     print('The Word is Not Palindromde')

#Write a program to check whether a number is present in given list
# x=int(input('Enter an Number: '))
# l=[23,67,12,90]
# if x in l:
#     print('The Number is Present')
# else:
#     print('The Number is Not Present')
#Write a program to check whether a key is present in a dictionary or not
# x=int(input('Enter an key: '))
# d={101:'Arun',102:'Amal',103:'Anu'}
# if d.keys:
#     print("Key is Present")
# else:
#     print("The Key is Not Present")

#Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
# s=input('Enter the Password: ')
# if len(s)>=8:
#     print("The password is Accepted")
# else:
#     print('The Password is Weak')

# write a program to check whether the user entered number is 2 digit/3 digit/ 4 digit number
# n1=int(input('Enter a number: '))
# if n1>=10 and n1<=99:
#     print('The Number is 2 Digit')
# elif n1>=100 and n1<=999:
#     print('The Number is  3 Digit')
# elif n1>=1000 and n1<=9999:
#     print('The Number is 4 digit')
# else:
#     print("Invalid")

# write a basic calculator program to perform arithametic operations
# n1=int(input('Enter a number: '))
# n2=int(input('Enter another number: '))
# op=input('Enter an Operator')
# op='*,/,+,//,%,/'
# if op=='+':
#     print(f"sum is :{n1+n2}")
# elif op=='-':
#     print(f"sum is :{n1 - n2}")
# elif op=='*':
#     print(f"sum is :{n1 * n2}")
# elif op=='/':
#     print(f"sum is :{n1 / n2}")
# elif op=='//':
#     print(f"sum is :{n1 // n2}")
# elif op=="%":
#     print(f" sum is :{n1%n2}")
# write a program to print the number of days in a month

# month=input('Enter a Month: ')
# l1=['January','March','May','July','August','October','December']
# l2=['April','June','September','November']
# l3=['February']
# if month in l1:
#     print("The Month Contains 31 Days")
# elif month in l2:
#     print("The Month Contains 30 Days")
# elif month in l3:
#     print('The Month Contains 28 or 29 days')

# write a program to print the grades based on the following criteria
grade=int(input('Enter the Marks: '))
if grade>=91 and grade<=100:
    print("Grade A")
elif grade>=81 and grade<=90:
    print('Grade B')
elif grade>=71 and grade<=80:
    print('Grade C')
elif grade>=61 and grade<=70:
    print('Grade D')
elif grade>=60:
    print('Grade E')

# write a program to check the following
# 1. a number is divisible by 2 and 3
# 2.a number divisible by 2 and not divisible by 3
# 3. a number divisible by 3 and not divisible by 2
# 4. a number not divisible by 2 and 3
n=int(input('Enter an Number: '))
if n%2==0:
    print('The Number is divisible by 2 and 3')
    if n%3==0:
        print('The Number is divisible by 3')
    else:
        print('The Number is Not divisible by 3 ')
else:
    print('The Number is  not Divisible by 2')
    if n%3==0:
        print('The Number is divisible by 3')
    else:
        print('The Number is Not Divisible by 3')

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

