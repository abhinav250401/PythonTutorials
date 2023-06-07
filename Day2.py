#Tip Calculator
#Day-2 Project
print("Welcome to tip calculator")
amount=input("What was the bill amount? \n")
tip=input("What percentage tip would you like to give? 10 12 or 15 ?\n")
persons=input("How many people to split the bill?\n")
tip_amt=float(amount)*float(tip)/100
total_amt=float(amount)+tip_amt
perhead=total_amt/float(persons)
print(f"Each person should pay: ${perhead}")
