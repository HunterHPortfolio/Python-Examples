import sys

#Hunter Holcombe
#Final Project - Milestone One
#September 22nd, 2018

#Initial user input - branch one
#Branch one determines which string output is generated
#this is based on the Rental Code input.
#The structure is if -> elif -> else
#This means if first condition is not true, proceed to elif
#condition, if neither is true perform the last statement
#Each statement setting rentalPeriod variable

#Variable one - variable name rentalCode, input string
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n')

if(rentalCode == "D"):
  rentalPeriod = input('Number of Days Rented:\n')
elif(rentalCode == "W" ):
  rentalPeriod = input('Number of Weeks Rented:\n')
else:
  rentalPeriod = input('Number of Days Rented:\n')
  
#Charge rates
#Variable two - variable name budgetCharge, input Float 
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	

#Variable three - variable name baseCharge
#int type - converts string to int values in order to calculate
#This is same for totalMiles variable
baseCharge = int(rentalPeriod) * int(budgetCharge) + 100
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart)

#Cost calculation - branch two
#Branch two is based on the Rental Code the user inputs
#This determines what price calculation to use
#This branch contains further branching
#The primary branch is if -> elif -> elif
#In each elif condition above contains a secondary branch if -> elif
#The secondary branches are based on the averageDayMiles (miliage)

if(rentalCode == "B"):
#Variable four - variable named mileCharge 
#In this instance it is set to a value based on calulation
#Further in the branch it gets modified to reflect different values
#This is dependant on the branching based on the rentalCode condition
    mileCharge = totalMiles * 0.25
  
elif(rentalCode == "D" ):
    #Variable five - in this exampled rentalPeriod data type changes
    #to calculate averageDayMiles as int
    averageDayMiles = totalMiles/int(rentalPeriod)
    
    #Branch three - mileCharge variable set to seperate
    #values based on the averageDayMiles condition
    #This branch is if -> elif meaning if the value
    #is less than/equal to 100, perform the code in that
    #statement, else if grater than 100, perform code
    #under the elif condition
    if(averageDayMiles <= 100):
        mileCharge = 0
    elif(averageDayMiles > 100):
        extraMiles = averageDayMiles - 100
        mileCharge = extraMiles * 0.25 * int(rentalPeriod)
        
elif(rentalCode == "W" ):
    averageDayMiles = totalMiles/int(rentalPeriod)
    
    #Branch four - similiar to branch three
    if(averageDayMiles <= 900):
        mileCharge = 0
    elif(averageDayMiles > 900):
        mileCharge = 10 * int(rentalPeriod)

#Rental summary displays values calculated above
print("Rental Summary")
print("Rental Code: " + rentalCode)
print("Rental Period: " + rentalPeriod) 
print("Starting Odometer: " + odoStart)
print("Ending Odometer: " + odoEnd)
print("Miles Driven: " + str(totalMiles))
print("Amount Due: $" + str(mileCharge) + "0")