#Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.

"""
def sort_str(s):
    s = s.lower().split()

    for i in s:
        ind = s.index(i)
        for j in s[ind+1:]:
            ind2 = s.index(j)
            if ord(j[0]) < ord(i[0]):
                s[ind], s[ind2] = s[ind2], s[ind]

    s = " ".join(s)
    return s     
"""
# ^ works but duplicate words makes them appear at end. .index() isnt reliable

def sort_str(s):
    s = s.lower().split()

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i][0] > s[j][0]: #just learnt, python can directly compare strings, my C origins could never accept this
                s[i], s[j] = s[j], s[i]

    s = " ".join(s)
    return s    
 

s = input("enter the string: ")

print(sort_str(s))