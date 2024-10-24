print("What type of vehicle would you like?")
print("1.Car")
print("2.Bike")
choice=int(input("Option 1 or 2?"))
if choice==1:
    print("1.SUV\n 2.Sedan\n")
    Choice_2=int(input("Enter your choice"))
    if Choice_2==1:
        print("You have selected an SUV, Congratulations!")
    else:
        print("You have selected a Sedan, Congratulations!")
elif choice==2:
    print("1.Scootie\n 2.Motorbike\n")
    Choice_3=int(input("Enter your choice"))
    if Choice_3==1:
        print("You have selected a Scootie, Congratulations!")
    else:
        print("You have selected a Motorbike, Congratulations!")
else:
    print("INVALID INPUT!")
    
    