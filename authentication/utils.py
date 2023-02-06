from string import digits
from random import choices
def generate_otp():
    otp = int(''.join(choices(digits, k=4)))
    return otp

