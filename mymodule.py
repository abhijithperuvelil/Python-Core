from calculator.operations import *
a=int(input("Enter the Number: "))
b=int(input("Enter the Number: "))
op=input('Enter the Operator: ' )
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
else:
    print('Invalid Operator')