#calculating how much time you have left if 90 is given
from calendar import month

age = int(input("Your Current Age: "))
yearsLeft = 90 - age
days = yearsLeft * 365
weeks = yearsLeft * 52
months = yearsLeft * 12

print(f"You have {days} days, {weeks} weeks or {months} months left")
