import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
input1 = int(input(" Enter a number "))

choices = random.sample(names, input1)
for choice in choices:
    print(choice)




# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
