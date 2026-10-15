# Worksheet 1.2: Task 1 Solution

import sys

try:
    numberEntered = int(input())
except (ValueError, EOFError):
    sys.exit("Error: Grade must be an integer between 0 and 100")

if not 0 <= numberEntered <= 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if numberEntered <= 39:
    print(numberEntered, "is a Fail")
elif numberEntered <= 69:
    print(numberEntered, "is a Pass")
else:
    print(numberEntered, "is a Distinction")





