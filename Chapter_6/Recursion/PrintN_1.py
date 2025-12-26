#recursive function
def show(n):
    if(n==0):
        return
    print(n,end=" ")
    show(n-1)

num = int(input("Enter a number to print : "))
show(num)
