# Task 3: Rock-Paper-Scissors Game
# Student: SHUBHASHNI SONI
# CodSoft Python Internship - June Batch C5
# Date: June 2026

import random

print("=== Rock Paper Scissors Game ===")
print("Instructions: Type rock, paper, or scissors")
print("-" * 40)

user_score = 0
computer_score = 0

while True:
    # Taking user input
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
    
    # Validating input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter rock, paper, or scissors")
        continue
    
    # Computer random selection
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    
    # Determining the winner
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You Win! 🎉")
        user_score += 1
    else:
        print("Computer Wins! 😢")
        computer_score += 1
    
    # Displaying current score
    print(f"Score - You: {user_score} | Computer: {computer_score}")
    
    # Asking to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! 😊")
        break
