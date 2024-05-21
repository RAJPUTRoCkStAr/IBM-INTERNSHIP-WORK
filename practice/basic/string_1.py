# a = "sumit singh" 
  #this is single line string 
# in python we write multi line strings with three single quotes like below we have written
# b= '''hello world
# this sumit kumar singh
# the next big programmer in python''' 
# print(b)
#Strings are Arrays
# print(a[1])
#Looping Through a String
# for i in a:
#  print(i)
#String Length
# name = "Worldisbeautiful"
# print(len(name))
# to check if the string exists
# txt = "kabhi kabhi toh lagta hai apun he bhagwan hai"
# if "apun" in txt:
#     print("yes apun is present in the string")
# Check if NOT
# txt = "yes apun is present in the string"
# if "sumit" not in txt:
#     print("no sumit is not there in the string")
# # Slicing
# name = "hello sumit"
# print(name[2:5]) #the first 2 is to start from index of 2 and than go till 5
# Slice From the Start
# name = "hello sumit"
# print(name[:5])
# Slice To the End
# name = "hello sumit"
# print(name[5:])
# Negative Indexing
# name = "hello sumit"
# print(name[-5:-2])
#capitalize sentence or word 
# txt = "lorem ipsum dolor sit amet consectetur adip occ"
# x = txt.capitalize()
# print(x)
# Upper Case
# name = "hello sumit"
# print(name.upper())
# Lower Case
# name = "HELLO SUMIT"
# print(name.lower())
#Remove Whitespace
# name = "hello sumit"
# print(name.strip())
#Replace String
# name = "hello sumit"
# print(name.replace('h','H'))
# Split String
# name = "hello sumit"
# print(name.split("u")) 
# endswith
# name = "hello sumit"
# print(name.endswith("sumit")) #this will tell you in boolean 
# name= "hello Sumit"
# print(name.swapcase()) #this will swap case of letter in string like it is capital it will change i to small and vice versa

# name = "hello Sumit"
# print(name.casefold()) #this is similar to lower only but it will force it to change to lower 
# s1 = "Straße"
# s2 = "STRASSE"

# print(s1.lower() == s2.lower())  # Output: False
# print(s1.casefold() == s2.casefold())

# name = "   hello Sumit"
# print(name.lstrip())

# name = "hello Sumit    "
# print(name.rstrip())

s = "Hello\tworld"
expanded_s = s.expandtabs(100) # here we are using \t for indentation with expandtabs in brackets give the number of words space you want
print(expanded_s)
