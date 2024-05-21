# python treats file differently as text or binary and this is important

# print(dir(os)) 
import os #here we are firstly importing the required os module

directory = r'C:\Users\sumit\OneDrive\Documents\python\learni\ile' #here we defined the directory path where we want to look for the directory
files = os.listdir(directory) #os.listdir(directory) we are looking for the files which are there already in the directory 
print(files) #printing all the files in that directory

file_path = os.path.join(directory, "hello.txt") # here we are joining the directory and our file which we already created there 
file = open(file_path,"a") # we are opening that file here
file.write("Hello, World!") # we are writing in that file
file = open(file_path,"r")
content = file.read() # here we are reading the content of the file
print(content) # printing all the content
os.remove(file_path) # remove thAT file
file = open("welcome.txt", "w")
file = open(file_path,"a") #
file.write("Hello, World!") # we are writing in that file
file = open(file_path,"r")
content = file.read() # here we are reading the content of the file
print(content)
file.close() # close that file

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists 



  