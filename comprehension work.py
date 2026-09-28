#Given  a list colors=['red','green','blue','orange']
# create a new list with first letter of each color
# create a new list with length of each color
# colors=['red','green','blue','orange']
# new=[]
# new=[i[0] for i in colors]
# print(new)
# new=[]
# new=[len(i) for i in colors]
# print(new)
# l=[1,2,3,4]
# new=[]
# new=[i**3 for i in l]
# print(new)
# l=[25,36,81,100]
# new=[]
# new=[i**0.5 for i in l]
# print(new)
#create a new list of first characters
#create a new list of last characters
#create a new list of reverse of each element
# colors=['red','green','blue','yellow','black']
# new=[]
# new=[i[0] for i in colors]
# print(new)
# new=[i[-1] for i in colors]
# print(new)
# new=[i[::-1] for i in colors]
# print(new)
#Given a list l=[23,78,12,56]
#Add 10 to each element in the given sequence
# l=[23,78,12,56]
# new=[]
# new=[i+10 for i in l]
# print(new)
##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# new=[]
# new=[i['email'] for i in l]
# print(new)
# # #create a new list with square root of each element
# l=[25,16,9,36]
# new=[]
# new=[i**0.5 for i in l]
# print(new)
# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
# # create a list of marks
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# names=[]
# names=[i for i in d.keys()]
# print(names)
# marks=[i for i in d.values()]
# print(marks)
#Given a list
# #create a list of string values
# #create a list of floats
# # #create a list of positive numbers
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# new=[]
# new=[i for i in l if type(i)==str]
# print(new)
# new=[i for i in l if type(i)==float]
# print(new)
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
#Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
# fruits=['apple','orange','pineapple','avocado','grapes']
# new=[]
# new=[i for i in fruits if len(i)>6]
# print(new)
# #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)
# Given s="python coding  is easy and fun"
# # create a new list with only vowels
# s="python coding"
# new=[]
# new=[i for i in s if i in 'aeiouAEIOU' ]
# print(new)
