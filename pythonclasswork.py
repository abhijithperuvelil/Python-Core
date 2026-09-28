s='I am Learning Python'
# length of the string
print (len(s))
#reverse of the string
print (s[::-1])
print (s[-1])
print (s[12])
print (s[2:15])
print (s+'programming')
s="python is a programming language"
print (s[10:])
print(s[-5:])

## complex data types
# declare a list of 5 colors
# add a new color 'yellow' to the list
# change the second color to black
# print the list in reverse order
# print the second last color
# print the number of colors
# print the updated list
lst=['red','blue','green']
print(lst)
lst.append('Yellow')
print(lst)
lst[1]='Black'
print(lst)
print(lst[::-1])
print(lst[-2])
print(len(lst))
print(lst)

s='Python coding is easy and fun'
print(len(s)) #len of the string
print(s[::-1]) # reverse of the string
print(s[-1])  #last character of the string

l=['Guitar','Piano','Violin','Drums','Flute']
l.append('Veena') # to add veena


l=['Cakes','Pizza','Biscut','Fruits','Rice']
l.append('Biriyani') # new list
l[1]='Dognut' # to change the second item

print(l[-1]) # last food item
print(len(l)) # number of food items

s = "python is a programming language"
print(s[11:]) # remove the first 10 characters
print(s[-5:]) # last 5 characters

# 1 given a set
s=set()
s={10,20,30,40}
s.add(50)
print(s)
#2.#Given a dictionary
student_grades={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}
print(student_grades['Charlie'])
student_grades['bob']=90
student_grades['Sam']=75
print(len(student_grades))
print(student_grades.keys())

##3.Given a dictionary
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
  'Amal':{'maths':40,'science':45,'english':48,'history':43},
           'Anu':{'maths':45,'science':46,'english':47,'history':49}}
print(student_marks['Amal']['history'])
student_marks['Arun']['maths']=35
print(student_marks)

