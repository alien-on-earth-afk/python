#a python code to remove unwanted chars from a string


def unwanted_string(strnig):
    result = ""
    for i in strnig:
        if i.isalpha() or i == " ":
            result += i
    return result


s = input("Enter the strings: ")

print(unwanted_string(s))

