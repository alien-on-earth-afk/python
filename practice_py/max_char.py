#a python code to find the maximum occurs chars

s = input("ENter the string: ")
d = {}


for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

for i in d:
    if d[i] == max(d.values()):
        print(f"{i}: {d[i]}")
        break
