#Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.

def ucolor(s1, s2):
    result = []
    for i in s1:
        if i not in s2:
            result.append(i)
    return result


s1 = input("Enter the colours 1: ").lower().split()
s2 = input("Enter the colours 2: ").lower().split()
print(ucolor(s1, s2))