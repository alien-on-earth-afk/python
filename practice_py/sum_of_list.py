#to add the elements of a list...idk why this was so far into the topic

l = input("Entter the list: ").split()
total = 0
for i in l:
    total += int(i)

print(total)