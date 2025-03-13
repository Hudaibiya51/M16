# Define a sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer"
}

# Get user input for the key
key = input("Enter the key to find its value: ")

# Check if the key exists and print the value
if key in my_dict:
    print(f"The value for '{key}' is: {my_dict[key]}")
else:
    print("Key not found in the dictionary.")