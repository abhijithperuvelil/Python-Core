# x=20
# print("Outside the Function",x)
# def a():                           ### GLOBAL
#     print("Inside the Function",x)
# a()
### LOCAL ###
# def b():
#     x=20
#     print('Inside the Function',x)
# b()
# print('Outside the Function',x)  ## ERROR because the variable can be used only in the inside function
#
### GLOBAL ###
def f():
    global x #### Used to Call from a function another functions
    x=20
    print(x)
f()
def g():
    y=30
    print(x)
    print(y)
g()