# Example 1: Append a single element
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Example 2: Append a list (adds the list as a single element)
numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)  # Output: [1, 2, 3, [4, 5]]  # Nested list!

# Example 3: Append different data types
mixed = [1, 'hello']
mixed.append(3.14)
mixed.append(True)
print(mixed)  # Output: [1, 'hello', 3.14, True]