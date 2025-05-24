#Write a Python program to multiply all the items in a list.

s = input("enter the lis: ").split()
total = 1
for i in s:
    if i.isdigit():
        total *= int(i)

print(total)
