import random

def rock_paper_scissor():
    print("Welcome to ROCK , PAPER , SCISSORS! ")
    print("Choices: rock, paper, scissors")

    options = ["rock","paper","scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter your choice or 'quit' to exit:").lower()
        if user_choice == 'quit':
            print("\nGAME OVER! ")
            print(f"Final score: You {user_score} - Computer {computer_score}")
            break
        if user_choice not in options:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose:{computer_choice}")

        if user_choice == computer_choice:
            print(f"It is a tie!")
        elif (user_choice == "rock" and computer_choice =="scissors")or\
             (user_choice == "scissor" and computer_choice == "paper")or\
             (user_choice == "paper" and computer_choice == "rock"):
             print(f"YOU WIN THIS ROUND!")
             user_score += 1
        else:
            print("COMPUTER WINS THIS ROUND!")
            computer_score += 1
        print(f"Score: You {user_score} - Computer {computer_score}")

rock_paper_scissor()