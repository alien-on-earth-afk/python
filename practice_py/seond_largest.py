#Write a Python program to find the second largest number in a list.

l = input("enter the list: ").split()
x = []
for i in l: 
    if not i.isdigit():
        print("only digits allowed")
        exit()
    else:
        x.append(int(i))
else:
    x.sort()
    print(x[len(x)-2])