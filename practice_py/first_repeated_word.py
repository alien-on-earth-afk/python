#a python code to print the first repeated word in a string

s = input("Enter the string: ").split()
print(s)

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print(f"the first repeated word is {s[j]}")
            exit()