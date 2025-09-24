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


    import threading
    def timed_input(prompt, timeout):
        result = [None]
        def inner():
            try:
                result[0] = input(prompt)
            except Exception:
                result[0] = None
        t = threading.Thread(target=inner)
        t.daemon = True
        t.start()
        t.join(timeout)
        if t.is_alive():
            return None
        return result[0]

    while True:
        mode = ''
        while mode not in ['classical', 'blitz']:
            mode = input("Would you like to play 'classical' Rock Paper Scissors or 'blitz'? (classical/blitz): ").strip().lower()
            if mode not in ['classical', 'blitz']:
                print("Invalid mode. Please enter 'classical' or 'blitz'.")
        print(f"You have selected {mode.title()} mode.")

        if mode == 'blitz':
            blitz_continue = True
            blitz_prompt_counter = 0
            play = input("Do you want to play Rock, Paper, Scissors Blitz mode? (yes/no): ").strip().lower()
            if play != 'yes':
                print("Thanks for playing!")
                break
            while True:
                print(f"Mode: {mode.title()}")
                user_choice = timed_input("Choose R, P, or S (7 seconds): ", 7)
                if user_choice is None:
                    print("Time's up! You did not respond in time.")
                    pclasslay_again = input("Play Again? (yes/no): ").strip().lower()
                    if play_again == 'yes':
                        break  # break to outer mode selection loop
                    else:
                        print("Thanks for playing!")
                        return
                user_choice = user_choice.strip().upper()
                if user_choice not in ['R', 'P', 'S']:
                    print("Invalid choice. Please enter R, P, or S.")
                    continue
                choice_map = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
                user_choice_full = choice_map[user_choice]
                computer_choice = random.choice(choices)
                print(f"Computer chose: {computer_choice}")
                if user_choice_full == computer_choice:
                    print("It's a tie!")
                    user_ties += 1
                elif (user_choice_full == 'Rock' and computer_choice == 'Scissors') or \
                     (user_choice_full == 'Paper' and computer_choice == 'Rock') or \
                     (user_choice_full == 'Scissors' and computer_choice == 'Paper'):
                    print("You win!")
                    user_wins += 1
                else:
                    print("You lose!")
                    user_losses += 1
                games_played += 1
                print(f"Your choice: {user_choice_full}, Computer's choice: {computer_choice}")
                print(f"Games played: {games_played}, Wins: {user_wins}, Losses: {user_losses}, Ties: {user_ties}")
                if not blitz_continue:
                    blitz_prompt_counter += 1
                    if blitz_prompt_counter % 5 == 0:
                        cont = input("Would you like to continue playing blitz mode? (yes/no): ").strip().lower()
                        if cont != 'yes':
                            print("Thanks for playing!")
                            return
                        blitz_continue = True
        else:
            while True:
                classical_rounds = 0
                while True:
                    play = input("Do you want to play Rock, Paper, Scissors? (yes/no): ").strip().lower()
                    if play != 'yes':
                        print("Thanks for playing!")
                        break
                    print(f"Mode: {mode.title()}")
                    user_choice_full = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
                    if user_choice_full not in choices:
                        print("Invalid choice. Please try again.")
                        continue
                    computer_choice = random.choice(choices)
                    print(f"Computer chose: {computer_choice}")
                    if user_choice_full == computer_choice:
                        print("It's a tie!")
                        user_ties += 1
                    elif (user_choice_full == 'Rock' and computer_choice == 'Scissors') or \
                         (user_choice_full == 'Paper' and computer_choice == 'Rock') or \
                         (user_choice_full == 'Scissors' and computer_choice == 'Paper'):
                        print("You win!")
                        user_wins += 1
                    else:
                        print("You lose!")
                        user_losses += 1
                    games_played += 1
                    classical_rounds += 1
                    print(f"Your choice: {user_choice_full}, Computer's choice: {computer_choice}")
                    print(f"Games played: {games_played}, Rounds played: {classical_rounds}, Wins: {user_wins}, Losses: {user_losses}, Ties: {user_ties}")
                play_again = input("Play Again? (yes/no): ").strip().lower()
                if play_again == 'yes':
                    continue  # restart classical session
                else:
                    print("Thanks for playing!")
                    break

if __name__ == "__main__":
    main()