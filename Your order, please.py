#https://www.codewars.com/kata/55c45be3b2079eccff00010f

from re import findall

def order(sentence):
    return ' '.join(word[1] for word in sorted([(int((findall(r"\d+", word)[0])), word) for word in sentence.split()]))
