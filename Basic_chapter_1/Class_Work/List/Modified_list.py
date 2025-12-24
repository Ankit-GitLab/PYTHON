# Changing elements
numbers = [1, 2, 3, 4]
numbers[0] = 10      # [10, 2, 3, 4]
numbers[-1] = 40     # [10, 2, 3, 40]

# Adding elements
numbers.append(5)    # [10, 2, 3, 40, 5]
numbers.insert(1, 15) # [10, 15, 2, 3, 40, 5]
numbers.extend([6, 7]) # [10, 15, 2, 3, 40, 5, 6, 7]

# Removing elements
numbers.remove(15)   # [10, 2, 3, 40, 5, 6, 7]
popped = numbers.pop()  # popped=7, list=[10, 2, 3, 40, 5, 6]
popped = numbers.pop(1) # popped=2, list=[10, 3, 40, 5, 6]
del numbers[0]       # [3, 40, 5, 6]
numbers.clear()      # [] (empty list)