C = 299792458
def main():
    mass = float(input("Enter the mass in kg: "))
    energy_in_joules: float = mass * (C ** 2)

    return energy_in_joules
if __name__ == "__main__":
    print(main())
