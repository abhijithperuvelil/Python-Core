# new_set={output for item in iterable if condtion}
## SET COMPREHENSION
# s='python coding is easy and fun'
# #create a new list with only vowels={}
# new={}
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)
# DICTIONARY COMPREHENSION
#given a new list [1,2,3,4]
#create a new dictionary with keys and values the square of each
# l=[1,2,3,4]
# new={}
# new={i:i**2 for i in l}
# print(new)
# l=[1,2,3,4]
# new={}
# new={i:i**3 for i in l}
# print(new)
#give a list
# l=[10,20,30,40]
#create a new dictionary where key as indexes and values are numbers
# l=[10,20,30,40]
# new={i: l[i] for i in range(0, len(l))}
# print(new)
# s='hello world'
# for i in s.split():
#     print(i)
#given a  string new dictionary where keys are words and values are length of each word
# s='python coding is easy and fun'
# new={i:len(i) for i in s.split()}
# print(new)