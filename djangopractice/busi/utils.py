#from .models import *
import re

def is_prime(number):
    
    if number <= 1:
        return False
        
    if isinstance(number, float):
        return False
    
    for element in range(2,number):
        if number % element == 0:
            return False
    return True
    
def check_email_format(email):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"