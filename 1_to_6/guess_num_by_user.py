import random
def guess():
    random_number = random.randint(1,10)
    guessed_num = 0
    while guessed_num != random_number:
        guessed_num =int(input(f'Guess a number between 1 and 10: '))
        if guessed_num < random_number:
            print("Sorry guess again. It's too low")
        elif guessed_num > random_number:
            print ("Sorry guess again. It,s too high")

    print (f'Congrats! you have guessed the number {random_number} correctly')

if __name__ == '__main__':
    guess()