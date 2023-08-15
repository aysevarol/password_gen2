import random
import string

# required lists
numbers = string.digits
special_chars = string.punctuation
lower = string.ascii_lowercase
upper = string.ascii_uppercase
chars = [numbers, special_chars, lower, upper]
all_chars = numbers + special_chars + lower + upper


def password_check():
    password_length = input("Enter the password length :")
    while not password_length.isdigit():
        print("Enter a integer")
        password_check()
    password_length = int(password_length)
    while password_length < 1:
        print("At least 1 character must be entered to create a password. ")
        password_check()
    return password_length


length = password_check()

include_uppercase = input("Do you want to include uppercase characters (y/n): ").lower() == 'y'
include_special = input("Do you want to include special characters (y/n): ").lower() == 'y'

our_chars = lower + numbers
if include_uppercase:
    our_chars += upper
if include_special:
    our_chars += special_chars

password = []
for i in range(length):
    password += [random.choice(our_chars)]

random.shuffle(password)
print("Generated password:", ''.join(password))
