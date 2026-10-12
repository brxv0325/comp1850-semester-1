# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
#the list has some values instead of being empty so runs until it's empty

# What features of Python does it rely on?
# non-empty list evaluates true, and empty lists evaluates false