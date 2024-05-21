# python is object oriented programming language
# A Class is like an object constructor, or a "blueprint" for creating objects.
# to create a class use class keyword 
# class name:
#     name = "Sumit"

# print(name)# the output will be <class '__main__.name'>
# p1 = name() # we are storing our class in p1
# print(p1.name) # like we can get the output as the value 


# the __init__()
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# class Person:
#     def __init__(self,name , age):
#         self.name = name
#         self.age = age

# p1 = Person("Sumit", 21)

# print(p1.name)
# print(p1.age)

#object Method
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# class Person:
#     def __init__(self,name , age):
#         self.name = name
#         self.age = age

#     def pri(self):
#         print("your name is ".upper() + self.name.upper  ", age is ".upper() + str(self.age)) 
# p1 = Person("Sumit", 21)
# p1.pri()


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
    def __init__(self,name , age): #in the place of self we can write anything no need to worry for that 
        self.name = name
        self.age = age
    def printin(abc): #here in this function we didn't used self instead i used abc and that's fine here
        print(abc.name.upper() + str(abc.age))

p1 = Person("Sumit", 21)
p1.age = 22
p1.printin() 

#if we want we can delete the p1 object also using del
# like del 
# del p1
# print(p1)


#__str__ in classes and objects 
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return "Person(name='{self.name}', age={self.age})"

# person = Person("Alice", 25)
# print(person) 
