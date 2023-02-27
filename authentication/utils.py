from string import digits
from random import choices
def generate_otp():
    otp = int(''.join(choices(digits, k=4)))
    return otp
print(generate_otp())


import random
import string


def generate_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)
generate_string(8)

