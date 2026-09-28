# i=1
# while(i<=10):
#     print(i)
#     i=i+1


# i=1
# while(i<=11):
#     print(i)
#     i=i+2

# i=2
# while(i<=10):
#     print(i)
#     i=i+2

# i=1
# while(i<=5):
#     print(i**2)
#     i=i+1

# i=5
# while(i>=1):
#     print(i)
#     i=i-1

# # #1,2,3,4,5,.....100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1

# # #1,3,5,7,9,11,13,15
# i=1
# while(i<=15):
#     print(i)
#     i=i+2

# #2,4,6,8,10,12
# i=2
# while(i<=12):
#     print(i)
#     i=i+2

# #1,4,7,10,13,16
# i=1
# while(i<=16):
#     print(i)
#     i=i+3

#10,20,30,40,50,60,70,80
# i=10
# while(i<=80):
#     print(i)
#     i=i+10

#3,6,9,12,15,18,21
# i=3
# while(i<=21):
#     print(i)
#     i=i+3

#5,4,3,2,1
# i=5
# while(i>=1):
#     print(i)
#     i=i-1

#8,6,4,2,0
# i=8
# while(i>=0):
#     print(i)
#     i=i-2

# #100,101,102,.....200
# i=100
# while(i<=200):
#     print(i)
#     i=i+1

#print all 4 digit numbers(1000-9999)

# i=1000
# while(i<=9999):
#     print(i,end=" ")
#     i=i+1
# print()

 # print those numbers that are divisible by 3 in the range (1,50)
# i=1
# while(i<=50):
#      if(i%3==0):
#         print(i, end=" ")
#      i=i+1
# print()

#print those 3 digits numbers that are divisible by 5 and 7
# i=100
# count=0
# while(i<=999):
#      if(i%5==0) and (i%7==0):
#         print(i, end=" ")
#      i=i+1
#      count=count+1
# print(count)

 #print those numbers in the range(100,200) which contains digit '3'
# i=100
# count=0
# while i<=200:
#     s=str(i)
#     if '3' in s:
#         print(i,end=" ")
#         count=count+1 ## count the numbers
#     i=i+1
# print(count)

# sum of series
# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)

# product of series
# i=1
# product=1
# while(i<=5):
#     product=product*i
#     i=i+1
# print(product)

# sum of first 10 even numbers
# i=2
# sum=0
# while(i<=10):
#     if i%2==0:
#        sum=sum+i
#     i=i+1
# print(sum)

# product of first 10 even numbers

# i=2
# product=1
# while(i<=10):
#     if (i%2==0):
#      product=product*i
#     i=i+1
# print(product)
#

# i=4
# while(i<=39):
#     print(i)
#     i=i+5


# i=1
# sum=0
# while(i<=11):
#     print(i)
#     sum=sum+i
#     i=i+2
#     print(sum)


# i=1
# product=1
# while(i<=50):
#     if (i%3==0) and (i%5==0):
#      product=product*i
#     i=i+1
# print(product)

# i=100
# count=0
# while i<=999:
#     if i%7==0:
#      count = count + 1
#     i = i+1
# print(count)

#factorial of a number
# n=int(input('Enter an Number: '))
# i=1
# fact=1
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print(fact)
#multiplication table of a number upto 10
# n=int(input('Enter an Number: '))
# i=1
# while(i<=10):
#     print(n,'*' ,i,'=',n*i)
#     i=i+1

### for loop
# l=['yellow','violet','Green']
# for i in l:
#     print(i)
#
# s={'id','name','place'}
# for i in s:
#     print(i)
#
# d={'id':100,'name':'Arun'}
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)
#
# t=(100,120,500,500)
# for i in t:
#     print(t)

# l=[12,34,56,45,89,16,69,33]
#print each numbers in list
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)
#print those numbers are even
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%2==0:
#         print(i)

#print those numbers are divisible by 5
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%5==0:
#         print(i)
# #print those numbers which contains 3
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     l=str(l)
#     if '3' in l:
#         print(i , end=" ")






# Given a dictionary
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# print each value
# print odd values
#
#
# Given a list l=["red",'green','orange','blue','black','yellow']
# print each color
# print color starting with 'b'
# print color whose length is greater than 5
#
#
# Given a list l=[10,'arun','amal',35,3.6,6.9,89]
# print  string values
# print float values

#given a string
# s='hello world'
# print each character
# s="hello world"
# for i in s:
#     print(i)
# # print those characters that are not vowel
# s="hello world"
# v="aeiou"
# for i in s:
#     if i not in v:
#        print(i)
# given a dictionary
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# # for i in d.values():
# #     print(d)
# for i in d.values():
#     if i%2!=0:
#         print(i)

# Given a list l=["red",'green','orange','blue','black','yellow']
# print each color
# print color starting with 'b'
# print color whose length is greater than 5
#
# l=["red",'green','orange','blue','black','yellow']
# for i in l:
# #     print(i)
# for i in l:
#     if i[0]=='b':
#         print(i)
# l=["red",'green','orange','blue','black','yellow']
# for i in l:
#     if len(i)>=5:
#         print(i)
# Given a list l=[10,'arun','amal',35,3.6,6.9,89]
# print  string values
# print float values
# l=[10,'arun','amal',35,3.6,6.9,89]
# for i in l:
#     if type(i)==str:
#        print(i)
#
# for i in l:
#     if type(i)==float:
#      print(i)

# l=[45,78,90,12,67]
# sum of list
# product of even values
# # count of odd values
# l=[45,78,90,12,67]
# sum=0
# product=1
# count=0
# for i in l:
#     sum=sum+i
#     print(sum)
# for i in l:
#     if i%2==0:
#         product=product*i
#         print(product)
# for i in l:
#     if i%2!=0:
#         count=count+1
#         print(count)

# i=1
# for i in range(1,10,2):
#     print(i)

# i=2
# for i in range(2,12,2):
#     print(i)

# i=1
# for i in range(1,30,3): #1,4,9,16,24
#     print(i)

# 4,9,14,19,24,....39
# i=4
# for i in range(4,44,5):
#      print(i)
 # 5,4,3,2,1
# for i in range(5,0,-1):
#     print(i)
# # 8,6,4,2,0
# for i in range(8,-1,-2):
#     print(i)
# 7,14,21,28,35,42
# for i in range(7,49,7):
#     print(i)
#for loop 100,200,300,10000
#1,8,27,64,125
# find all 3 digits numbers that are divisible by 3
#colors =['red','green',blue,yellow,black]
# for i in range(100,1001,100):
#     print(i)
#
# for i in range(1,6):
#     print(i**3)
#
# # find all 3 digits numbers that are divisible by 3
# for i in range(100,1000):
#     if i%3==0:
#         print(i)
# # #colors =['red','green',blue,yellow,black]
# colors =['red','green','blue','yellow','black']
# for i in colors:
#   print(i[::-z1])

# n="1234"
# for i in str(n):
#     print(i)
#sum of digits in a number
#
# n=1234
# sum=0
# for i in str(n):
#     sum=sum+int(i)
#     # print(i)
# print(sum)
#given a list l=[1,2,3,4]
# # new list with squares of the number
# new=[]
# l=[1,2,3,4]
# for i in l:
#     new.append(i**2)
# print(new)
# set
# new=set()
# l=[1,2,3,4]
# for i in l:
#     new.add(i**2)
# print(new)
# print(type(new))
# s='hello world'
# new=''
# vowel='aeiouAEIOU'
# for i in s:
#     if i in vowel:
#         new=new+i
# print(new)

#dictionary
#create a new dictionary where keys are numbers and values are square of each number
# l=[1,2,3,4]
# new={}
# for i  in l:
#     new[i]=i**2
# print(new)
# #reverse of a string
# s='hello'
# reverse=''
# for i in s:
#     reverse=i+reverse
# print(reverse)
#
# n=1234
# s=''
# for i in str(n):
#     s=i+s
# print(s)
# s='hello'
# for i in s:     for break statement
#     if i=='l':
#         break
#     print(i)
#
# s='hello'
# for i in s:
#     if i=='l':
#         continue
#     print(i)

# l=[25,67,34,78,17,44,82]
# print all numbers
# stops the loop when i>50
# skip all even numbers
l=[25,67,34,78,17,44,82]
# for i in l:
#     print(i)
# for i in l:
#     if i>50:
#         break
#     print(i)
# for i in l:
#     if i%2==0:
#         continue
#     print(i)
# Given a list colors=['red','green','yellow','blue','orange','black']
#print all colors
#print those colors starting with 'b' #blue black
#print the first color starting with 'b' #blue

#skips all colors starting with 'b
# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     print(i)
# for i in colors:
#     if i[0]=='b':
#         print(i)
# for i in colors:
#     if i[0]=='b':
#         print(i)
#         break
# for i in colors:
#     if i[0] == 'b':
#         continue
#     print(i)
#
# s="python coding is easy and fun"
# for i in s:
#     print(i)
#     if i=='s':
#        break

