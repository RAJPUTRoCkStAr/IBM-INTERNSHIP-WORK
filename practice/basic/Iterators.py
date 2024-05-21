# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:
# next is also considered as a function here that give the next value each time
# fruits = ["apple", "orange", "banana"]
# myfruits = iter(fruits)

# print (next(myfruits))
# print (next(myfruits))
# print (next(myfruits))

#we can also print iterator using iter and next function 
# fruits = "apple"
# myfruits = iter(fruits)

# print (next(myfruits))
# print (next(myfruits))
# print (next(myfruits))
# print (next(myfruits))
# print (next(myfruits))


# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# class MyNumbers:
#   def __iter__(self):
#     self.a = 2
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 2
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#StopIteration statement
#To prevent the iteration from going on forever, we can use the StopIteration statement.
class addingnumber:
    def __iter__(self):
        self.fn = 2
        return self
    def __next__(self):
        if self.fn <= 22:
            x = self.fn
            self.fn +=2
            return x 
        else:
            raise StopIteration
        
multi = addingnumber()
mul = iter(multi)

for x in mul:
    print(x)
