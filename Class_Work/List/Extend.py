# Example 1: Extend with a list
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'date'])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Example 2: Extend with different iterables
numbers = [1, 2, 3]
numbers.extend([4, 5])      # List
numbers.extend((6, 7))      # Tuple
numbers.extend({8, 9})      # Set
numbers.extend("ab")        # String (adds characters)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b']

# Example 3: Extend with range
numbers = [1, 2]
numbers.extend(range(3, 6))
print(numbers)  # Output: [1, 2, 3, 4, 5]