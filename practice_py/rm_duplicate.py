#to remove the duplicate words in a string 
s = input("Enter the string: ").split()

seen = set()
r = []
for i in s:
    if i not in seen:
        seen.add(i)
        r.append(i)
r = " ".join(r)
print(r)
