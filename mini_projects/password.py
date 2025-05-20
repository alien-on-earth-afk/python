x = 0
p1 = ""
while(1):
    if x == 1:
        p2 = input("confirm password: ")
        if p1 == p2:
            print("Your password is", p2)
            break
        else:
            print("Wrong! try again.")
            x = 0
            continue
    p = input("Enter password: ")
    ok = ""
    if len(p) <= 4:
        print("Password too short.")
        continue
    elif len(p) >= 16:
        print("Password too long.")
        continue
    for i in p:
        if not i.isalnum():
            print("You cant use special characters")
            continue
        if i.islower():
            ok = ok + "l"
        if i.isupper():
            ok = ok + "u"
        if i.isdigit():
            ok = ok + "d"
        if i.isalpha():
            ok = ok + "a"
    if "a" not in ok:
        print("You have to use characters")
        continue
    elif "l" not in ok or "u" not in ok:
        print("you have to use a combination of lower and upper characters")
        continue
    elif "d" not in ok:
        print("you have to use a digit")
        continue
    else:
        x = 1
        p1 = p1 + p




