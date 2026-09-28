# def sqr(n):
#     x=n*n
#     return x
# a=sqr(6)
# print(a)
# Sum of 2 numbers
s = lambda a, b: a + b
# Product of 3 numbers
p = lambda a, b, c: a * b * c
# Cube of a number
c = lambda a: a ** 3
# first letter of a string
first = lambda s: s[0]
print(first('HEllo'))
# length of a string
l = lambda l: len(l)
print(l('HEllo'))
# reverse of a string
r=lambda s:s[::-1]
# name value from dictionary
name = lambda d: d['name']
print(name({'name':'arun'}))
second = lambda l: l[1]
add = lambda a: a + 10
