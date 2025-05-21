#take input from user
#count each word's occurence

s = input("Enter the string: ").split()
print(s)

d = {}
for i in range(len(s)):
    if s[i] not in d.keys():
        d[s[i]] = 1
    else: 
        d[s[i]] += 1

print(d)

