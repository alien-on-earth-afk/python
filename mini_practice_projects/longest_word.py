#find the longest word in a list

s = input("Enter the list: ").split()
print(s)
l = s[0]
for i in range(1, len(s)):
    if len(s[i]) > len(l):
        l = s[i]

print(f"The longest word is {l}")
print(f"it is {len(l)} chars long")

