"""
def swap_case(s):
    sword = ""
    for i in s:
        if i.islower():
            sword = sword + i.upper()
        else:
            sword = sword + i.lower()
    return sword
#working^
"""

#try2
def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    s = "".join(s)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)