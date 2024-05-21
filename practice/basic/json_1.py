# JSON is text, written with JavaScript object notation.
# json import will not work if you give the name of the file is as it's importer name.
 
# importing of json to json to python first and to do so we need 
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

#importing of json module 
# import json
# some random json in the variabele x 
# x = '{"name": "sumit","age":21,"city":"varanasi"}' #always remember to use (' ') this first and then this(" ") otherwise an error will be raised
# converting everything from json to python
# print(json.loads(x))
#lets print it out

# import json 
# print(dir(json))

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# lets import json first

# import json

# x = {
#     "name":"sumit",
#     "age":21,
#     "city":"varanasi"
# }

# print(json.dumps(x))

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=4)) # here the indent mean that indentation of the object
# Use the separators parameter to change the default separator:

# print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use the sort_keys parameter to specify if the result should be sorted or not:
# print(json.dumps(x, indent=4, sort_keys=True))