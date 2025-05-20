import textwrap

s = input("Enter the string: ")
""""
l = textwrap.wrap(s, 2)
n = len(l)
if(n == 1 and len(l[0]) <= 1):
    word = " "
else:
    word = l[0] + l[n-1]
print(word)
"""
#nice but there gotta be better way
#wait string slicing lol

if len(s) < 2:
    word = " "
else:
    word = s[:2] + s[len(s)-2:]
print(word)
