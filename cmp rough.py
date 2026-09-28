# Create a new list containing the last letter of each fruit.
# fruits = ['apple', 'banana', 'mango', 'grapes']
# new=[]
# new=[i[-1] for i in fruits]
# print(new)
# Create a new list containing the number of characters in each city name.
# cities = ['Delhi', 'Kochi', 'Mumbai', 'Chennai']
# new=[]
# new=[len(i) for i in (cities)]
# print(new)
# l = [49, 64, 81, 121]
# # Create a new list containing the square root of each number.
# new=[]
# new=[i**0.5 for i in l]
# print(new)
# Create a new list containing the reverse of each animal name.
# animals = ['tiger', 'lion', 'elephant', 'rabbit']
# new=[]
# new=[i[::-1]for i in animals]
# print(new)
# Subtract 5 from each element and create a new list.
# l = [15, 28, 39, 42]
# new=[]
# new=[i-5 for i in l]
# print(new)
# l = [
#     {'id': 1, 'name': 'Rahul', 'age': 22},
#     {'id': 2, 'name': 'Anu', 'age': 24},
#     {'id': 3, 'name': 'Akhil', 'age': 21}
# ]
# # Create a new list containing only the names.
# new=[]
# new=[i['name']for i in l]
# print(new)
from multiprocessing.spawn import is_forking

# d = {'Rahul': 80, 'Anu': 92, 'Akhil': 75, 'Neha': 88}
# # Create a new list containing only the marks greater than 80.
# new=[]
# new=[i for i in d.values() if i>80]
# print(new)
# Create a new list containing only the integer values.
# l = [45, 'python', -12, 8.5, 'java', 0, 6.7]
# new=[]
# new=[i for i in l if type(i)==int]
# print(new)
# Create a new list containing the vegetables whose length is less than 6.
# vegetables = ['carrot', 'pea', 'cabbage', 'onion', 'potato']
# new=[]
# new=[i for i in vegetables if len(i)>6]
# print(new)
# Create a new list containing only the consonants.
# s = "Programming is Awesome"
# vowel='aeiouAEIOU'
# new=[]
# new=[i for i in s if i not in vowel]
# print
# Define a function that takes 2 lists as arguments and returns a new list containing the elements that are present in the first list but not in the second list.
list1 = [12, 24, 36, 48]
list2 = [36, 48, 60, 72]
def dup(list1,list2):
    new=[]
    for i in list1:
        if i not in list2:
            new.append(i)
    return new

a=dup(list1, list2)
print(a)