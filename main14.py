medical_cause= input("Do you have a medical cause? Either Yes or No")
attendance= int(input("What is your attendance?"))
if medical_cause=="Yes":
    print("allowed :)")
else:
    if attendance >75:
        print("allowed :)")
    else:
        print("Not allowed :(")
        
