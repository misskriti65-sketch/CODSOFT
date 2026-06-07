# Task 1: Simple Calculator
# Student: SHUBHASHNI SONI
# CodSoft Python Internship - June Batch C5
# Date: June 2026

print("=== Simple Calculator by Shubhashni ===")
print("Operations: +  Addition")
print("            -  Subtraction") 
print("            *  Multiplication")
print("            /  Division")
print("-" * 35)

try:
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose operation (+, -, *, /): ")

    # Performing calculation
    if operator == '+':
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
        
    elif operator == '-':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
        
    elif operator == '*':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
        
    elif operator == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
            
    else:
        print("\nInvalid operator! Please use only +, -, *, /")

except ValueError:
    print("\nError: Please enter valid numbers only!")

print("\nThank you for using the calculator 😊")
