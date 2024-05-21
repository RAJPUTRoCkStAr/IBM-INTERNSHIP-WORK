# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.



# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string

#findall 
# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

#search 
# import re

# txt = "The  Srain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())

# split()
# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt,2)
# print(x)

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# (12, 17) here 12 is the where S is and 17 is the total value of that string

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 
#The rain in Spain

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Spain