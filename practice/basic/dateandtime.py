# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime 
x = datetime.datetime.now()
print(x)
#output => 2023-07-02 23:20:43.907390 its showing me year-month-day hour:minute:second:microsecond

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))