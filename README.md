# Bill Splitter & Tip Calculator

bill = float(input("Enter total bill amount: ₹"))
tip = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
per_person = total_bill / people

print("\n----- Bill Summary -----")
print("Bill Amount:", bill)
print("Tip Amount:", tip_amount)
print("Total Bill:", total_bill)
print("Number of People:", people)
print("Each Person Pays:", per_person)Enter total bill amount: ₹1000
Enter tip percentage: 10
Enter number of people: 4

----- Bill Summary -----
Bill Amount: 1000.0
Tip Amount: 100.0
Total Bill: 1100.0
Number of People: 4
Each Person Pays: 275.0

