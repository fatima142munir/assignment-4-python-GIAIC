def main():
    numbers: list[int] = [3,4,6,8]
    add_num: int = 0
    for number in numbers:
        add_num += number
    return add_num

if __name__ == "__main__":
    print(main())
