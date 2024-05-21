# we write list in square brackets
# marks = [95,98,97]
# print(marks[-3])  # in python writing - means that it should start from back
# print(marks[0:4]) # in python : means that from which to which index you want value

# now lets perform some operation
# marks.append(99) #it is to append our list append will add the value in last
# marks.insert(0,89) # it is to add the value where we want using list index
# print (89 in marks) #it will check if 89 exists in our list
# print(len(marks)) #to get the length of the list
# marks.clear() #it will clear the list
# print(marks)
# del marks[1] #using del you need to specify the index 
# marks.remove(95)
# marks.pop(2)
# print(marks)

#sort is buy default case sensitive resulting in all capital letters being sorted before lower case letters:
# marks.sort()
# print(marks)
# Sort Descending
# marks.sort(reverse=True) #reverse the list
# print(marks)

#we can customize the sort function using
##key = function
# def myfunc(n):
#   return abs(n - 50) #abs = absolute number in python
# here is subtracting from thislist from 50 so thats why its written abs(n-50)
# where n = 100,50,65,82,23
# thelist = 100-50=50
# thelist = 50-50=0
# thelist = 65-50=15
# thelist = 82-50=32
# thelist = 23-50=27
# so the output is [50, 65, 23, 82, 100]
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# this is another function that we can create  
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


#copy() method is to copy a list because list cannot be copied like list1 = list2 because it will  will only be a reference to list1, and changes made in list1 will automatically also be made in list2..
# fruits = ["apple", "banana", "cherry"]
# market = fruits.copy()
# print(market)


# Another way to make a copy is to use the built-in method list().
# fruits = ["apple", "banana", "cherry"]
# mar = list(fruits)
# print(mar)


#there are 2 ways we can join two lists together
#using append()
#another one using + 
list1=["apple", "banana", "cherry"]
list2 = ["bmw","audi","diamond"]
#lets use first method to join two lists together
# list1.append(list2)
# print(list1)
#its another of joining two lists together with append()
# for x in list2:
#   list1.append(x)

# print(list1)
#lets use second method to join two lists together
# list3 = list1 + list2
# print(list3)