# Program to eliminate repeated lines from a file

# Creating the output file
with open('UpdatedFile.txt', 'w') as outputFile:
    # Reading the input file
    with open('Repeated.txt', 'r') as inputFile:
        # Holds lines already seen
        lines_seen_so_far = set()
        print("Eliminating duplicate lines....")
        
        # Iterating through each line in the file
        for line in inputFile:
            # Checking if line is unique
            if line not in lines_seen_so_far:
                # Write unique lines in output file
                outputFile.write(line)
                # Adds unique lines to lines_seen_so_far
                lines_seen_so_far.add(line)
