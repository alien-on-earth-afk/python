# a python script to encrypt a string with caesar encryption
result = ""
s = input("Enter the string: ").lower()
shift = int(input("The number of shit: "))


for i in range(len(s)): 
    if s[i].isalpha():
        if ord(s[i]) < ord('a') + shift:
            shifted = chr(ord('z') - (ord(s[i]) - ord('a')))
        else:
            shifted = chr(ord(s[i]) - shift)
        result += str(shifted)
    else:
        result += s[i]

print(result)
