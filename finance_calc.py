# SIS PROYECT DAY 1
# Goal: Calculate monthly savings
print("Welcome to your financial calculator")

# Use float (allow decimal values) and (int for whole numbers) and you use input when the computer listen to you 
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
    
# Prueba de contribución - 16 de febrero de 2026
# Update: Testing my first green square!
# This is a simple financial calculator that helps users determine their monthly savings based on their income and expenses. It provides feedback on their financial situation, encouraging them to save more if they are breaking even or spending more than they earn.
    print("This is a test of the contribution feature. I am adding a green square to indicate that this code has been updated.")

 