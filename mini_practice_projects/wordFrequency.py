freq = {}
s = input("Enter the string: ")

for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)