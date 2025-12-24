# Using list() constructor
from_range = list(range(5))  # [0, 1, 2, 3, 4]
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_tuple = list((1, 2, 3))  # [1, 2, 3]

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]