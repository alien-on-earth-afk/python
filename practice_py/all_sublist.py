#Write a Python program to generate all possible sublists of a list.

def all_subsets(lst):
    subsets = [[]]

    for elem in lst:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [elem])  # add current element to existing subsets14
        subsets += new_subsets  # add these new subsets to the list

    return subsets


lis = input("Enter the list: ").split()
subs = all_subsets(lis)
for s in subs:
    print(s)

