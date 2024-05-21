print("program to find next and previous palindrome of number ")

def palindrome(num):
    return str(num) == str(num)[::-1]
def next(num):
    num += 1
    while not palindrome(num):
        num += 1
        return num
def previous(num):
    num -= 1
    while not palindrome(num):
        num -= 1
    return num
number = int(input("enter a number"))
nextnumber = next(number)
previousnumber = previous(number)

print(f"the next number is {nextnumber}")
print(f"the previous number is {previousnumber}")

# print("Program to check if a number is a palindrome or not")

# # Get the user input
# user_num = int(input("Enter a number: "))

# # Store the original number to compare later
# original_num = user_num

# # Reverse the number
# reversed_num = 0
# while user_num > 0:
#     digit = user_num % 10
#     reversed_num = reversed_num * 10 + digit
#     user_num = user_num // 10

# # Check if the original number and reversed number are the same
# if original_num == reversed_num:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")

