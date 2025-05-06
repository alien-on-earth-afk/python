#program to calculate bmi

weight = int(input("Enter Weight(kg): "))
height = float(input("Enter Height(m): "))
bmi = (weight/(height**2))
print(f"Your BMI is {round(bmi, 2)}")
if(bmi<=18.4):
    print("You're Underweight")
elif(bmi<=24.9 and bmi>=18.5):
    print("Youre normal")
elif(bmi>=25 and bmi<=29.9):
    print("You're Overweight")
elif(bmi>= 30):
    print("You're obese")
