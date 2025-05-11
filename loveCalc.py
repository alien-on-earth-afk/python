# i know this one might seem dumb but well its in exercise so cant avoid it
# this is like those discord games where we check 2 names with "true love"

person1 = input("Enter name of person 1: ").lower()
person2 = input("Enter name of person 2: ").lower()
combined = person1 + person2
t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')
l = combined.count('l')
o = combined.count('o')
v = combined.count('v')

x = t+r+u+e
y = l+o+v+e
print(f"Your love count is {x}{y}%")