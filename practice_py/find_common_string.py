#Write a Python program to find the common first string that appear in two given strings.

def sim_string(s1, s2):
    result = ""
    x = 0
    for i in s1:
        if i == " " or (i in s2 and not i in result):
            result += i
            x = 1
        elif x == 1:
            break
    return result

s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")

print(sim_string(s1, s2))