def is_disarium(number):
    # Convert number to string to get digits
    digits = str(number)
    
    # Calculate the sum of digits raised to their respective positions
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    
    # Check if sum equals the original number
    return disarium_sum == number

# Get user input
num = int(input("Enter a number: "))

# Check and display result
if is_disarium(num):
    print(f"{num} is a Disarium Number.")
else:
    print(f"{num} is not a Disarium Number.")