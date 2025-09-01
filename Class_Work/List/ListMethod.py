numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting
numbers.sort()              # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Reversing
numbers.reverse()           # [1, 1, 2, 3, 4, 5, 6, 9] reversed

# Copying
copy1 = numbers.copy()      # Shallow copy
copy2 = numbers[:]          # Another way to copy

# Counting
count = numbers.count(1)    # 2 (number 1 appears twice)

# Finding index
index = numbers.index(4)    # 3 (first occurrence of 4)