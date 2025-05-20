import textwrap

s = input("Enter the string: ")
l = textwrap.wrap(s, 2)
n = len(l)
if(n == 1 and len(l[0]) <= 1):
    word = " "
else:
    word = l[0] + l[n-1]
print(word)
