import textwrap
"""
def wrap(string, max_width):
    i = max_width
    while(i<len(string)):
        string = string[:i] + '\n' + string[i:]
        i+= max_width+1
    return string
"""
#working ^

def wrap(string, max):
    string = textwrap.fill(string, 4)
    return string

if __name__ == '__main__':
    string, max_width = input("Enter string: "), int(input("Enter max width: "))
    result = wrap(string, max_width)
    print(result)