# Ask the user for a number
curr_value = int(input("Enter a number: "))

# Loop until the value reaches or exceeds 100
while curr_value < 100:
    curr_value = curr_value * 2  # Double the number
    print(curr_value)  # Print the value on the same line
