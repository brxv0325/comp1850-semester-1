
# function implementation

def rectangle_area(length, width):  # define suitable input data
    # ...               # implement the function
    return length * width  # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(5, 3)}")   # provide suitable data matching your inputs

# A function that accepts an integer value and returns a list of even integers between 0 and that value.

def evenInts(integer_value):
    """
    returns all even umbers wheen 0 and n
    """
    while type(integer_value) == int:
        listOfEven = []
        evenNum = 0 + 2
        listOfEven.append(evenNum)
        if evenNum == integer_value:
            break
    else:
        return "Value must be an integer"