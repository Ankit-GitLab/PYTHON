tup = (1,4,9,16,25,36,49,64,81,100)
x = 16 #search this element
 
idx = 0
for val in tup:
    if(val == x):
        print("yes found at index : ",idx)
        break
    idx += 1
