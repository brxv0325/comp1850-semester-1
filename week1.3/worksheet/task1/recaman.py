# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

number = 0
previousNum = 0
step = 1
sequence = [0]
# Your code for the Recaman Sequence
while len(sequence) < L:
    result = previousNum - step

    if result > 0 and result not in sequence:
        previousNum = result
    else:
        previousNum = previousNum + step

    sequence.append(previousNum)
    step += 1

    
# You should store the sequence in an appropriate data structure named 'sequence'



# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence