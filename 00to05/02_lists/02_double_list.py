def main():
    numbers: list[int] = [3,4,6,8]
    for i in range(len(numbers)):
        numbers[i] *= 2
    print(numbers)

if __name__ == "__main__":
    main()