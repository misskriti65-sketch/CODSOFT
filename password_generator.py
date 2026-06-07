# Task 2: Random Password Generator
# Student: SHUBHASHNI SONI
# CodSoft Python Internship - June Batch C5
# Date: June 2026

import random
import string

print("=== Random Password Generator ===")
print("-" * 35)

try:
    length = int(input("Enter password length: "))
    
    if length < 4:
        print("\nError: Password length should be at least 4 characters!")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        print(f"\nYour generated password is: {password}")
        print("Note: Save this password safely!")

except ValueError:
    print("\nError: Please enter a valid number!")

print("\nThank you for using Password Generator 😊")
