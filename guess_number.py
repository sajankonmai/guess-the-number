import random
import sys

from colorama import Fore, Style


def guess_number(min_num=1, max_num=10):
    # Main game loop
    while True:
        num = random.randint(min_num, max_num)
        attempt = 0

        # Display game instructions
        print(Fore.BLUE + '******************************************************')
        print('        Welcome to guessing the number game!')
        print(f'      Please guess the number between {min_num} and {max_num}.')
        print('******************************************************\n' + Style.RESET_ALL)

        # Guessing loop
        while True:
            try:
                guess = int(input('Enter your guess: '))

                # Validation: Check if the guess is within the range
                if guess < min_num or guess > max_num:
                    print(Fore.RED + f'⚠ Out of range! Please guess the number between {min_num} and {max_num}.'
                          + Style.RESET_ALL)
                    continue  # Skip the loop

                attempt += 1

                # Check user's guess and provide hints if it's incorrect
                if guess < num:
                    print(Fore.YELLOW + '⬇ Low! Try guessing higher.' + Style.RESET_ALL)
                elif guess > num:
                    print(Fore.YELLOW + '⬆ High! Try guessing lower.' + Style.RESET_ALL)
                else:
                    # Correct guess
                    attempt_txt = "attempt" if attempt == 1 else "attempts"
                    print(Fore.GREEN + f'🏆 Congratulations! You guessed the number in {attempt} {attempt_txt}.\n' +
                          Style.RESET_ALL)
                    break  # Exit guessing loop

            except ValueError:
                print(Fore.RED + '⚠ Please enter a valid number.' + Style.RESET_ALL)

        # Play again loop
        while True:
            play_again = input('Do you want to play again? (Y/N): '
                               ).strip().lower()  # Remove whitespace and convert it to lowercase

            if play_again in ('yes', 'y'):
                print(Fore.CYAN + '\nStarting a new game...\n' + Style.RESET_ALL)
                break  # Start a new game
            elif play_again in ('no', 'n'):
                print(Fore.MAGENTA + '\n*** Game over! Thank you for playing. ***' + Style.RESET_ALL)
                sys.exit()  # Exit the game
            else:
                print(Fore.RED + "⚠ Invalid input! Please enter 'Y' or 'N'." + Style.RESET_ALL)


if __name__ == "__main__":
    guess_number(1, 50)
