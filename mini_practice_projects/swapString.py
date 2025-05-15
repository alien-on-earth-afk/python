

def swap_case(s):
    sword = ""
    for i in s:
        if i.islower():
            sword = sword + i.upper()
        else:
            sword = sword + i.lower()
    return sword

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)