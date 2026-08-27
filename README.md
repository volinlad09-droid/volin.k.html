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
print("Each Person Pays:", per_person)
