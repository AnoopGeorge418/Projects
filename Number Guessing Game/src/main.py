# genrate a random number
# ask for input from user
# if input is bigger number -> too high
# if input is smaller number -> too low
# if it is correct - > correct

import random
import sys

def random_number_generator():
    random_no = random.randint(1, 100)
    return random_no

def main():
    print('Welcome to random number generator game')
    number_guess = random_number_generator()

    while True:
        try:
            guess = int(input('Enter your guess: '))
            if guess == number_guess:
                print(f'You got it correct! Hooray...')
                break
            elif guess > number_guess:
                print(f'Oops {guess} is Too High! Try again...')
            elif guess < number_guess:
                print(f'Oops {guess} is Too Low! Try again...')

        except ValueError:
            print("Please enter number as guess.")
        except (KeyboardInterrupt, EOFError):
            print('Existing from game. Goodbye!')
            sys.exit()

if __name__ == "__main__":
    main()