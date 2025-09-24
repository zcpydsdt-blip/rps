# 1. Turn on the application.
# 2. Prompt the user if they would like to play Rock, Paper, Scissors.
# 3. If the user says yes, prompt them to choose Rock, Paper, or Scissors.
# 4. Randomly select Rock, Paper, or Scissors for the computer.
# 5. Compare the user's choice with the computer's choice and determine the winner.
# 6. Display the choices and the winner.
# 7. Ask the user if they want to play again.
# 8. Display a counter of the number of games played and the number of wins, loses and ties for the user.
# 9. Repeat steps 2-8 until the user chooses to exit.

def main():
    import random

    choices = ['Rock', 'Paper', 'Scissors']
    user_wins = 0
    user_losses = 0
    user_ties = 0
    games_played = 0

    while True:
        play = input("Do you want to play Rock, Paper, Scissors? (yes/no): ").strip().lower()
        if play != 'yes':
            break

        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            user_ties += 1
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            user_losses += 1
        games_played += 1
    print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")
    print(f"Games played: {games_played}, Wins: {user_wins}, Losses: {user_losses}, Ties: {user_ties}")

    print("Thanks for playing!")
if __name__ == "__main__":
    main()