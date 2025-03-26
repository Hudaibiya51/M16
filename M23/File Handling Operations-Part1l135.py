# Write in file using with() function
with open('Codingal.txt', 'w') as file:  # Use lowercase 'w' for write mode
    file.write("Hi! I am Penguin and I am 1 yr old.")

# Split file into words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()  # Read the lines from the file
    print("Words in this file are....")
    for line in data:
        words = line.split()  # Split the line into words
        print(words)  # Print the words
