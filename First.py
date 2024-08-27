#Welcome to the tip calculator
#What was the total bill ?
#How much tip you would like to give ? 10,12 or 15? 
#How many people to split the bill 
#Each person should pay : ____

print("Welcome to the til calculator")

bill = input("What was the total bill? ")
bill = float(bill.strip("$"))
tip  = float(input("How much til you would like to give ? 10,12 or 15? "))
spllit = int(input("How many people to split the bill ? " ))

tip = bill*tip/100
bill = bill + tip
bill = bill/spllit

print("Each person should pay : $", round(bill,2))