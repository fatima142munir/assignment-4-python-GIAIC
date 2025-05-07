
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for i in range(MIN_VALUE,N_NUMBERS+1):
        print(f"{i} - {random.randint(MIN_VALUE, MAX_VALUE)}")



if __name__ == '__main__':
    main()