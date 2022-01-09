#https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    for l in string.ascii_lowercase:
        if l not in s.lower():
            return False
    return True
