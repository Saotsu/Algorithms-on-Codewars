#https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    s = "".join(w.capitalize() for w in s.split())
    return "#"+s if 0 < len(s) < 140 else False
