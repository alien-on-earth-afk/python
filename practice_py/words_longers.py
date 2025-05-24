#Write a Python program to find the list of words that are longer than n from a given list of words.

s = input("Enter the string: ").split()
n = int(input("enter the n: "))

result = ""

for i in s:
    if len(i) > n:
        result.append(i)
        
print(result)