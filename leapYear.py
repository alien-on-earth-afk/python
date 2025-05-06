year = int(input("Enter Year: "))

if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} isnt a leap year")