#write a program to find the simple interest
p=1000
n=2
r=6
si=(p*n*r)/100
print(si)
#write a program to interchange to values
from tempfile import tempdir
a=2
b=3
temp=a # using third variable
a=b
b=temp
print(a,b)

a=2 #without using a variable
b=3
a,b=b,a
print(a,b)

#without using a variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print('The value of a is ',a,'The Value of b is ',b)
