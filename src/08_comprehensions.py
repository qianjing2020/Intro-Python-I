"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
lst = list(range(0, 6))
y = [item for item in lst]
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
lst = list(range(0, 10))
y = [item**3 for item in lst]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [item.upper() for item in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
x = input("Enter comma-separated numbers: ").split(',')

lst = [item for item in x if int(item)%2==0]
print(f'print out elements that are even numbers {lst}')

lst=[item for item in x if x.index(item) % 2 == 0]
print(f'print out elements with even index {lst}')

# What do you need between the square brackets to make it work? 
y = []
print(y)
# I am not sure what the question is asking. Vague. 
y = ['Even without anything between the square brackets, y is still printable, at least with python 3.7.4 here.']
print(y)
