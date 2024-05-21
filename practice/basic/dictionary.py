#ib=n dictionary there is key and its value {"english" this the key : 98 and this the value}
marks = {"english" : 98 ,"maths":96}
# print(marks["maths"]) #this is the way we can get the value of maths
# marks["cs"] = 99 #this is to add the one more key and value in dictionary
# print(marks) # to change the value just redeclare it and give its value you want to change
# print(len(marks)) #this is to get the length of dictionary
# we can access the items of a dictionary by referring to its key name, inside square brackets:
# print(marks["english"])
# this is the method by get
# print(marks.get("english")) 
# The keys() method will return a list of all the keys in the dictionary.
# print(marks.keys())
# Get Values
# The values() method will return a list of all the values in the dictionary.
# print(marks.values())
# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# print(marks.items()) 

# there is update function in python that can add as well as update the dictionary
# marks.update({"maths": 2020})
# print(marks)

#to delete there is lot of some of them are

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.pop("model") #this is delete model from  dictionary
# print(thisdict)
# thisdict.popitem() # this will delete item from dictionary
# print(thisdict)
# del thisdict["model"] #this is delete model from  dictionary
# print(thisdict)
# thisdict.clear() #this will clear full dictionary
# print(thisdict)