class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def getname(cls,string):
        name,age = string.split(',')
        return cls(name,int(age))
personname = person.getname("sumit,21")
print(personname.name,personname.age)