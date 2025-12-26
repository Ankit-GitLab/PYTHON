list = ["Ankit", "Ravi", "Vishal", "Sunny", "Vedant"]

def print_Ele(list, idx = 0):
    if(idx == len(list)):
        return 
    
    print(list[idx],end=" ")
    return print_Ele(list, idx+1)

print_Ele(list)

