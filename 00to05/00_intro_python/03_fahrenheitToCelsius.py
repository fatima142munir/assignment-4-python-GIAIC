def main():
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (temp_in_fahrenheit - 32) * 5.0 / 9.0
    return f"{temp_in_fahrenheit} Fahrenheit is equal to {degrees_celsius} Celsius"

if __name__ == '__main__':
    print(main())
