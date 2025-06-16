#Write a Python program to generate all sublists of a list.

def subl(lst):
    sublist = [[]] #<- empty set bc all subsets hve it 

    for e in lst:
        curr = []

        for s in sublist:
            curr.append(s + [e])

        sublist.extend(curr)

    return sublist


lst = input("Enter the list: ").split()


print("Sublists: ")
print(subl(lst))

    