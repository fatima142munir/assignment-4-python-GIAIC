def print_even_numbers():
    print("even numbers between 1 to 20")
    for i in range(21):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    print_even_numbers()