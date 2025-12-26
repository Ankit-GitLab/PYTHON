def sum(n):
    if(n==0):
        return 0

    return n + sum(n-1)

num = int(input("Enter a number to print sum of natural number : "))
print(sum(num))
    