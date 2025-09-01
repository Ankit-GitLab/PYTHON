my_list = ['a', 'b', 'c', 'd', 'e']

# Positive indexing
print(my_list[0])    # 'a'
print(my_list[2])    # 'c'

# Negative indexing
print(my_list[-1])   # 'e' (last element)
print(my_list[-2])   # 'd' (second last)

# Slicing
print(my_list[1:4])  # ['b', 'c', 'd']
print(my_list[:3])   # ['a', 'b', 'c']
print(my_list[2:])   # ['c', 'd', 'e']
print(my_list[::2])  # ['a', 'c', 'e'] (every 2nd element)