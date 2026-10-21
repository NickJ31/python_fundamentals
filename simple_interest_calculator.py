# Simple Interest Calculator
# This program calculates simple interest based on the principal amount,
# interest rate, and time.

print("Simple Interest Calculator")
print("------------------------------")

while True:
    try:
        principal = float(input("Enter the principal amount: "))
        if principal <= 0:
            print("Please enter an amount greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        rate = float(input("Enter the interest rate (in %): "))
        if rate < 0:
            print("Interest rate cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        time = float(input("Enter the time in years: "))
        if time <= 0:
            print("Please enter a time greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Please enter your name.")
    elif len(name) > 100:
        print("Name must be 100 characters or less.")
    else:
        break

name = name.title()
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("------------------------------")
print("Calculated Results")
print("------------------------------")
print("Customer Name:", name)
print("Principal Amount: $", round(principal, 2))
print("Interest Rate:", rate, "%")
print("Time:", time, "years")
print("Simple Interest: $", round(simple_interest, 2))
print("Total Amount: $", round(total_amount, 2))
print("Thank you for using the Simple Interest Calculator!")
