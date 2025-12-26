collection = set()

collection.add(1)# add in set
collection.add(2)
collection.add((1,2,3))
collection.add("ankit")
collection.add("RIYA")

collection.remove(2) #remove from the set

print(len(collection))

print(collection.pop()) #remove the random value
print(collection.pop()) #remove the random value


collection.clear() # remove all element from set

print(len(collection))