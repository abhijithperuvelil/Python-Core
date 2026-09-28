# s={1,2,3,4,5}
# s.add(10) # to add a single element to the set
# s.update((4,5,6,7,8)) # to add a sequence to existing set
# # print(s)
# s.remove(10) # to remove a single element form the set
# s.discard(8) # to remove a single element form the set (remove and discard have same)
# # s.pop() # it will remove any value from the set
# # print(s)
# s={1,2,3,4,5}
# t={4,5,6,7}
# s.union(t) # it will combine both sets
# # print(s.union(t))
# # l=(s.intersection(t)) # it will print the common values in two sets
# # print(l)
# # l=(s.intersection(t)) # it will print the common values in two sets
# # print(l)
# # a=s.difference(t)
# # print(a) # it will print the elements in the first set compared to another set
# a=s.symmetric_difference(t) # it will remove the common elements from the two sets
# # print(a)
#### QUESTIONS ???? >>> ??? ###
# 1.Given a list =[1,1,2,3,3,5] remove the duplicates
# l = [1, 1, 2, 3, 3, 5]
# print(list(set(l)))
# 2.remove duplicates without using set () order should be preserved
# l=[1,1,2,3,3,4]
# new = []
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
# # 3. given 2 list
# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))
