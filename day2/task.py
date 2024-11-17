print("Welcome to the tip calculator!")

bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the total bill with the tip

percentage = tip / 100
bill_per_person = bill * percentage
total_bill = bill + bill_per_person

# Calculate the amount each person should pay
finally_paid = total_bill / people

print(f"Each person should pay: ${round(finally_paid, 2)}")
