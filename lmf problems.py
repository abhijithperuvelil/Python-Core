# Q1. Create a lambda function to find the square of a number.??
# def square(n):
#     x = (lambda x: x**2 )
#     # print(x)
#     return x(n)
# def even(a):
#     m=(lambda x:x%2==0)
#     return m(a)
#     # n = 10
# a=even(3)
# print(a)
# To find the largest number
# def large(a,b):
#     m=lambda a,b : 'A is greater' if a>b else 'B is Greater'
#     # s="A is Greater"
#     return m(a,b)
# a=large(5,10)
# print(a)
# length of the string
# s = "python"
# print((lambda s: len(s))(s))
# square of a number
# l = [2, 3, 4, 5]
# print(list(map(lambda x:x**2,l)))
# l = [2, 3, 4, 5]
# new=[]
# new=(list(map(lambda x:x+10,l)))
# print(new)
# l = [2, 4, 6, 8]
# new=list(map(lambda x:x*3,l))
# print(new)
# l = [2, 3, 4, 5]
# new=list(lambda x:x%2==0,l)
# print(new)
# words = ['cat', 'elephant', 'dog', 'python']
# new=list(map(lambda x:len(x),words))
# print(new)
# words = ['apple', 'banana', 'orange', 'grapes']
# new=list(map(lambda x:x[-1],words))
# print(new)
# words = ['python', 'java', 'html', 'css']
# new=list(map(lambda x:x.capitalize(),words))
# print(new)
from hmac import new

# l = [10, 15, 20, 25, 30, 35]
# print(list(filter(lambda x:x%2==0,l)))
# l = [11, 20, 31, 40, 51, 60]
# print(list(filter(lambda x:x%2!=0,l)))
# l = [10, 45, 23, 67, 32, 89]
# print(list(filter(lambda x:x>40,l)))  
# l = [10, 30, 20, 45, 15, 50]
# print(list(filter(lambda x:x<25,l)))
# l = [10, 12, 15, 17, 21, 25, 30]
# print(list(filter(lambda x:x%3==0,l)))
# words = ['cat', 'apple', 'dog', 'orange', 'sun']
# new=(list(filter(lambda x:len(x)>4,words)))
# # print(new)
# words = ['apple', 'banana', 'animal', 'dog', 'ant']
# print(list(filter(lambda x:x[0] =='a',words)))
# words = ['python', 'java', 'green', 'blue', 'orange']
# print(list(filter(lambda x:x[-1]=='n',words)))