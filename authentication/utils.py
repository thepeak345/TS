from string import digits
from random import choices


def generate_otp(count):
    otp = int(''.join(choices(digits, k=count)))
    return otp
