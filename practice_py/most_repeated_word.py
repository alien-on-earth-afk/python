#to print the most repeated word

s = input("Enter the string: ").split()
d = {}

for i in range(len(s)):
    if s[i] in d.keys():
        d[s[i]] += 1
    else:
        d[s[i]] = 1

for i in d:
    if d[i] == max(d.values()):
        print(i)
        break
