#https://www.codewars.com/kata/525f47c79f2f25a4db000025

from re import findall

def valid_phone_number(phone_number):
    return findall(r'^\(\d{3}\)\s\d{3}\-\d{4}$', phone_number) != []
