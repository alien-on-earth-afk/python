#to add the elements of a list...idk why this was so far into the topic
#only numbers woukd be considered now so you cant add a "hello" in the list to crash it 
l = input("Entter the list: ").split()
total = 0
for i in l:
    if i.isdigit():
        total += int(i)

print(total)

