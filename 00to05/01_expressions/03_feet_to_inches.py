import math
def main():
    measurement_in_feet= float(input("Enter the measurement in feet: "))
    convert_feet_in_inches = math.floor(12 * measurement_in_feet)
    return convert_feet_in_inches

if __name__ == "__main__":
    print(main())
