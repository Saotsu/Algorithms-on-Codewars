#https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    msg = ""
    for l in message:
        if l.islower():
            msg += letters[(ord(l)-84)%26]
        elif l.isupper():
            msg += letters[(ord(l)-52)%26].upper()
        else:
            msg += l
    return msg
