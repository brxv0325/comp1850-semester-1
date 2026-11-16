import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
input1 = int(input("Enter a number"))
while input1 > 0:
    choice = random.choice(names)
    print(choice)
    input1 -= 1

# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
