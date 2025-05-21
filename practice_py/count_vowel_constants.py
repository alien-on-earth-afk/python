#a program to count vowels and constants
string = input("Enter the string: ").lower()

vowels = "aeiou"
constants = 0
vowel_count = 0

for i in string:
    if i.isalpha():
        constants += 1
        if i in vowels:
            vowel_count += 1

print("Number of vowels: ", vowel_count)
print("Number of constants: ", constants - vowel_count)



