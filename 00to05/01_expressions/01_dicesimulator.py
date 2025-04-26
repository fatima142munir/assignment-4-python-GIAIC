import random
def roll_dice():
    for i in range(3):
        print("roll" + str(i +1))
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(total)


def main():
    roll_dice()

if __name__ == "__main__":
    # print(main())
    main()