import random

def main():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Die one is {die1} and die two is {die2}, total is: {total}")

if __name__ == "__main__":
    main()