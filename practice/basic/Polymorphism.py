#polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# function like len() is nothing but polymorphism


# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name. lets see that in below code
# lets do it 
# class car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("drive")
# class plane:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("fly")
# class boat:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("float")
# mycar = car("bmw","a30")
# myplane = plane("akasa","a3030")
# myboat = boat("wooden boat","qt34")

# for x in (mycar, myplane, myboat):
#     x.move()
# here we are getting only value that we want to from function but we are not able to see the value of the class to do see the below code

# class car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("drive")
# class plane:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("fly")
# class boat:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def move(self):
#         print("float")
# mycar = car("bmw","a30")
# myplane = plane("akasa","a3030")
# myboat = boat("wooden boat","qt34")

# for x in (mycar, myplane, myboat):
#     print(x.name)
#     print(x.model)
#     x.move()

# Inheritance Class Polymorphism
# yes we can do it 
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!"+self.brand+"!"+self.model)

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()