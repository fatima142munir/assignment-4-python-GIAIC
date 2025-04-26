def main():
    number1 = int(input("enter first number: "))
    number2 = int(input("enter second number: "))
    division : int = int(number1 / number2)
    remainder = number1 % number2
    return f"The result of this division is {division} with a remainder of {remainder}."

if __name__ == "__main__":
    print(main())
