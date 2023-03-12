from string import digits
from random import choices


def generate_code(count):
    codebox = int(''.join(choices(digits, k=count)))
    return codebox
