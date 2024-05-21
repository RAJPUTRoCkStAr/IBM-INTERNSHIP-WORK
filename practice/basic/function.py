# function in pythob
# there are 3 types of functions 
# 1-> In-built function => they are already there in python
# 2-> module function => related folders and are there in python we can use them using import
# 3-> user defined function => which we create and use in function

# import math 
# print(dir(math)) # this will show all the function available function in that module 
# from math import sqrt # if we want to use a specific function python
# print(sqrt(16)) #this will squreroot of 16
# from math import * #by this we can use everything available in math

#now lets make our function
# syntax 
#def function_name(parameter):
# def print_sum(first,second):
#     print(first + second)
# print_sum(1,2)
# we can also declare value in parameter like below code
# def print (first,second=4):
#     print(first + second)
# print(1,'')


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# def myfunction():
#     pass

#recurison
# Python also accepts function recursion, which means a defined function can call itself.
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1) # k = 1,2,3,4,5 
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n""Recursion Example Results")
# print(tri_recursion(6))