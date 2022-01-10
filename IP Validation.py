#https://www.codewars.com/kata/515decfd9dcfc23bb6000006

def is_valid_IP(strng):
    strng = strng.split(".")
    if len(strng) != 4:
        return False
    for n in strng:
        if not n.isdigit():
            return False
        elif len(n) >= 2 and any([n[0] == "0", int(n) > 255, int(n) < 0]):
            return False
    return True
