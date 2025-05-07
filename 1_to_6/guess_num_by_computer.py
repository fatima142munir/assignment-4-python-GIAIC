import random


def computer_guess():
    low = 1
    high = 100
    feedback = ""
    guess = 0

    print("Think of a number between 1 and 100, and I'll try to guess it!")

    while feedback != "c":
        guess = random.randint(low, high)  # Computer makes a guess
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1  # Reduce the upper bound
        elif feedback == "l":
            low = guess + 1  # Increase the lower bound

    print(f"Yay! I guessed your number {guess} correctly!")


if __name__ == "__main__":
    computer_guess()