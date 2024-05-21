class person:
    # name = "sumit"
    # age = 21
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print (f"{self.name} is and he {self.age} is year old")

a = person("elon",56)
a.info()