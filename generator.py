# random password generator using python
import numbers
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

combination = lower + upper +number + symbols
print("password length to generate:")
pass_length = int(input())

password = "".join(random.sample(combination, pass_length))

print("Generated password is : " , password )
