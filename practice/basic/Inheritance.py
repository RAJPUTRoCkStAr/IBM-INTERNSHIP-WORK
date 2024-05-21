# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# class person: #first we need to create a class 
#     def __init__(self,name,rollno): 
#         self.name = name
#         self.rollno = rollno
#     def perfunction(your):
#         print("Your name is ->" + your.name+"\n" +"Your rollno is ->"+ str(your.rollno))
# #lets create a child class now

# class personson(person): # we are creating a class and letting it inherit from the parent class name person 
#     pass # here we are giving the class because we dont want to insert something into this class
# iden =personson("Sumit",21)
# iden.perfunction()


#as now we were successful to get child class inhert parent class 
# now we need to get that by __init__() method and also there is more function that is super() we directly inhert all the properties from parent to child class 

# class myclass:
#     def __init__(self,name,rollno):
#         self.name = name 
#         self.rollno = rollno
#     def stu(self):
#         print ("Your name is ->" + self.name+"\n" +"Your rollno is ->"+ str(self.rollno))
# class stud(myclass):
#     def __init__(self,name,rollno):
#         super().__init__(name,rollno) #we can either use super() function or just do it by writing class name
#         # myclass.__init__(name,rollno)

# p1 = stud("sumit",21)
# p1.stu()
        
## that's how i do below codes the above is done with self created function and below one is done using __str__()
# class myclass:
#     def __init__(self,name,rollno):
#         self.name = name 
#         self.rollno = rollno
#     def __str__(self):
#         return "Your name is ->" + self.name+"\n" +"Your rollno is ->"+ str(self.rollno)
# class stud(myclass):
#     def __init__(self,name,rollno):
#         super().__init__(name,rollno) #we can either use super() function or just do it by writing class name
#         # myclass.__init__(name,rollno)

# p1 = stud("sumit",21)
# print(p1)

#lets make another an try to insert some properties in it 

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def don(self):
#         print("person name is " + self.name+" and age is " + str(self.age))
# class per(person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#         self.graduationyear = 2019

# x = per("Mike", "Olsen")
# print(x.graduationyear)

# the conculsion is that we can add any property to the child class and to access that we have 2 methods one is above and other one is below

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def don(self):
        print("person name is " + self.name+" and age is " + str(self.age))
class per(person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.graduationyear = year
    def boy(self):
        txt = ("person name is " + self.name+" and age is " + str(self.age)+" and year is " + str(self.graduationyear))
        x = txt.capitalize()
        print(x)

x = per("Mike", 21,2019)
x.boy()
