#a program to check palindrome

word = input("Enter a word: ")

l = len(word)
r = l-1
x=0
for i in range(l//2):
    if word[i] == word[r]:
        x = 1
        r -= 1
    else:
        x = 0
        break
if x == 1:
    print("Is a palindrome")
elif x == 0:
    print("Is not a palindrome")