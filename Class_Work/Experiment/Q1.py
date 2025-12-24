# Simple String Manipulation Program

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Indexing
print("First character of s1:", s1[0])
print("Last character of s1:", s1[-1])

# Slicing
print("First 5 characters:", s1[:5])
print("Reversed string:", s1[::-1])

# Concatenation
s3 = s1 + " " + s2
print("Concatenated string:", s3)

# Substring Search
sub = input("Enter substring to search in first string: ")

if sub in s1:
    print("Substring found at index:", s1.find(sub))
else:
    print("Substring not found.")
