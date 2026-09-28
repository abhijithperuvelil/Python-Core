# # write a program to check whether the number is even or Odd
# n = int(input("Enter a Number: "))
# if n%2==0:
#     print("The Number is Even")


# write a program to check whether the number is positive or negative
# n = int(input("Enter a Number: "))
# if n>0:
#     print("The Number is Positive")
# else:
#     print("The Number is Negative")

# write a program to check whether the number is even or Odd
# n = int(input("Enter a Number: "))
# if n%2==0:
#     print("The Number is Even")
# else:
#     print(f"{n} The Number is Odd")
    # Write a program to check the number is divisible 3
# n = int(input("Enter a Number: "))
# if n % 3 == 0:
#      print("The Number is Divisible by 3")
# else:
#      print(f"{n} The Number is Not Divisible By 3")

# write a program to display a name if the entered name contains letter 'n' else
# name=input('Enter an Name:')
# if 'n' in name:
#     print("Name is ,",name)
# else:
#     print("No")

# write a program to display a name if the name entered start with n
#else display No
# name=input('Enter an Name:')
# if  name[0]=='n':
#     print("Name is :",name)
# else:
#     print('No')
# write a program to display a location name if the entered location contains word 'land' else print no
loc=input('Enter an location:')
if  'land' in loc:
    print('location is', loc)
else:
    print('No')
# write a program to check whether number is divisible by 5 and ends with 5
x=int(input('Enter an Number'))
if x%5==0 and x%10==5:
    print("The Number is Divisble 5 ")
else:
    print("NO")
# write a program to find the greatest of two numbers
n1=int(input('Enter an Number1'))
n2=int(input('Enter an Number1'))
if n1>n2:
 print("The Number is  Greater",n1)
else:
    print('The Number is Greater',n2)

# elif else condition write a program to check whether the number is positive or negative , Zero
n1=int(input('Enter an Number1: '))
if n1>0:
    print("The Number is Positive")
elif n1<0:
    print("The Number is Negative")
else:
    print("The Number is Zero")

# write a program to find the greatest of Three numbers
n1=int(input('Enter an Number1'))
n2=int(input('Enter an Number3'))
n3=int(input('Enter an Number3'))
if n1>n2 and  n1>n3:
 print("The N1 is  Greater",n1)
elif n2>n3 and n2>n1:
    print('The N2 is Greater',n2)
else:
    print('The N3 is Greater',n3)
# write a program to check whether the person is eligible to vote
a=int(input('Enter the Age of the Person: '))
if a>=18:
    print("The Person is Eligible")
else:
    print("The Person is Not Eligible")
# write a program to check whether the number is even or Odd or invalid
n = int(input("Enter a Number: "))
if (n%2==0):
    print("The Number is Even")
elif (n%2!=0):
    print(f"{n} The Number is Odd")
else:
    print("Invalid")

