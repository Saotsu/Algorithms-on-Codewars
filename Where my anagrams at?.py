#https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    s = [w for w in words if sorted(w) == sorted(word)]
    return s if s else []
