# Creating a list
fruits = ["apple", "banana", "cherry"]

print("Original list:", fruits)

# Add element at the end
fruits.append("orange")
print("After append:", fruits)

# Insert element at index 1
fruits.insert(1, "grape")
print("After insert:", fruits)

# Remove element by value
fruits.remove("banana")
print("After remove:", fruits)

# Remove last element using pop
popped = fruits.pop()
print("After pop:", fruits)
print("Popped element:", popped)