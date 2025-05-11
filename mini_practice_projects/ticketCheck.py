# a program to check if user's height is eligible for ride
# create a bill for user according to his age
# if user wants to click pictures then charge extra


age = int(input("Enter your age: "))
clickPic = input("Do you want to click pictures?(yes/no): ").lower()
height = int(input("Enter your Height(ft): "))
total = 0
if(height<=3):
    print("Sorry You can't ride.")
else:
    print("You are eligible for ride")
    if age<=12:
        total = 150
    elif age<18:
        total = 250
    else:
        total = 500
    print("Your Ticket Price is: ", total)

    if clickPic == "yes":
        total += 50
    elif clickPic != "no":
        print("Invalid input for pictures")

    print(f"Your Total is: {total}")
