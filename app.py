import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"
        if not play_again:
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))

play_game()