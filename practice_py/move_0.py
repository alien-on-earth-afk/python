#Write a Python program to move all zero digits to the end of a given list of numbers.

lst = input("enter the number: ").split()
lst = [int(x) for x in lst]
print(lst)

# for i in range(len(lst)):
#     for j in range(i, len(lst)-1):
#         if(lst[j] == '0'):
#             lst[j+1], lst[j] = lst[j], lst[j+1]

# print(lst)
#works but two loops needed, i can count zero and add manually

result = []
nzero = []
zeros = 0
for i in lst:
    if i != 0:
        nzero.append(i)
    else:
        zeros += 1

result = nzero + [0] * zeros
print(result)