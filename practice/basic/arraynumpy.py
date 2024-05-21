# python does not support Array but we have a library for that is
# NumPy library.
import os 
import numpy as np

numpy_dir = os.path.dirname(np.__file__)
contents = os.listdir(numpy_dir)

for item in contents:
    print(item) 

#  to get the full item of numpy 