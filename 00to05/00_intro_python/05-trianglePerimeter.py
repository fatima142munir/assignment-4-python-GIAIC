def main():
    side1= float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    return f"The perimeter of triangle is {int(side1 + side2 + side3)}"

if __name__ == "__main__":
    print(main())