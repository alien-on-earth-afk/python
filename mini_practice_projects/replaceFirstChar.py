s = input("Enter the string: ")
ch = s[0]
for i in range(1, len(s)):
    if s[i] == ch:
        s = s.replace(ch, '$')
print(s)
