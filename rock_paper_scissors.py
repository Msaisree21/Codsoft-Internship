import random
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        print("You win!")
        return 1, 0  # User wins, computer loses
    elif winner == "computer":
        print("Computer wins!")
        return 0, 1  # User loses, computer wins
    else:
        print("It's a tie!")
        return 0, 0  # Tie, no score change
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_round_score, computer_round_score = play_round()
        user_score += user_round_score
        computer_score += computer_round_score
        print(f"Current score: You - {user_score}, Computer - {computer_score}")
        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
print("Welcome to Rock-Paper-Scissors!")
play_game()