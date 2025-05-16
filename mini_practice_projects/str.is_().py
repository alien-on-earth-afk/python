if __name__ == '__main__':
    s = input("Enter the string: ")
    
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    
    for c in s:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.islower():
            has_lower = True
        if c.isupper():
            has_upper = True
            
print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)


