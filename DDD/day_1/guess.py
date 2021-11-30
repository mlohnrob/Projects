# A = list(map(int, input().split()))
# element = int(input())

import sys

def guesser(guess=500, prev_guess=500):
    print(f"prev_guess: {prev_guess}")
    print(guess)
    answer = input()
    print(guess)
    if answer == "lower":
        new_prev_guess = guess
        guess -= (guess - prev_guess) // 2
        guesser(guess, prev_guess=new_prev_guess)
    elif answer == "higher":
        new_prev_guess = guess
        if guess != 500:
            guess += (guess - prev_guess) // 2
        else:
            guess = 750
        guesser(guess, prev_guess=new_prev_guess)
    elif answer == "correct":
        print(f"Guess: {guess} is corect")
        sys.exit()
    else:
        sys.exit()

if __name__ == "__main__":
    guesser()
