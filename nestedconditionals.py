#Take input for the students that he can attend the exam
medical_cause = input("did you have  medical cause Y or N: ")
#Take input of the attendance
atten = int(input("enter the attendance of the student: "))

#checking the user input prediciting output accordingly

if medical_cause == 'Y' : #checkig the condition 1
    print ("You are allowed")
else: 
    if atten>=75: #checking the condition 2
        print("Allowed")
    else:
        print("Not allowed")
        
    # Take input of number of units consumed from the user
    units = int(input("Please enter number of Units you consumed: "))
    
    #Check conditions of units consumed
    #Then calculate amount and surcharge accordingly
    #surcharge is the tax value
    
    #Check for units less than 50
    if(units < 50):
        amount = units*2.60
        surcharge = 25
    
    #Check for units less than 100
    elif(units <= 100):
        amount = 130*3.25
        surcharge = 35
    
    #Check for units less than or equal to 200
    elif(units <= 200):
        amount = 130*5.26
        surcharge = 45
        
    #Check for all the cases other than mentioned
    #When units consumed are more than 200
    else: 
        amount = units*8.45
        surcharge = 75
        
    #Calculate and display the total electricity bill
    #Total amount = amount + surcharge
    total = amount+surcharge
    print("\nElectricity Bill = %.2f" %total)
    
#Select your ride
print("Select your ride: ")
print("1. Bike")
print("2. Car")
#take input of number 1 or 2
#select your ride
choice = int(input("Enter your choice: "))
#User entering option 1
if(choice == 1): #condition 1 outer if statement
    print("What type of bike? ")
    print("Scooty\n")
    print("Scooter\n")
    
    #Condition for selecting the type of bike
    choice2 = int(input("Enter your choice2: "))
    if choice2==1: #inner if statement
        print("You have selected scooty")
    else:
        print("You have selected scooter")

    #User entering option 2
elif(choice == 2): #outer elif statement
    print("what type of car")
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("enter your choice3: "))
    if choice3==1: #inner if statement
        #condition for selecting the type of car
        print("you have selected sedan")
    else:
        print("You have selected XUV")
    
else: #outer else statement
    print("Wrong choice!!")