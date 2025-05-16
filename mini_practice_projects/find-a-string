def count_substring(string, sub_string):
    count = 0
    l = len(sub_string)
    for i in range(len(string) - l + 1):
        if sub_string in string[i:i+l]:
            count += 1
    return count

if __name__ == '__main__':
    string = input("Enter string: ").strip()
    sub_string = input("Enter sub_string: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)


    #count = string.count(sub_string)
    #print(count)