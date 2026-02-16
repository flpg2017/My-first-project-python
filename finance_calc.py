# SIS PROYECT DAY 1
# Goal: Calculate monthly savings
print("Welcome to your financial calculator")

# Use float to allow decimal values(int for whole numbers) and you use input when the computer listen to you 
Income = float(input("Enter your monthly income (Soles): "))
Expenses = float(input("Enter your monthly expenses (Soles): "))

# Calculate monthly savings
Savings = Income - Expenses

print(f"Your monthly savings is: {Savings} Soles")

if Savings > 0:
    print("Great job! You are saving money.")
elif Savings == 0:
    print("You are breaking even. Consider finding ways to save more.")
else: 
    print("You are spending more than you earn. Consider reducing your expenses.")