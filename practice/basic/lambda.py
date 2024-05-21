# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# x = lambda a : a + 10
# print(x(5)) # the output will be 15
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11)) # here the output will be 22 

#let use lambda to make a funtion that give square of the value

# def mysqr(k):
#     return lambda a: a*k
# square = mysqr(2)
# print(square(2))