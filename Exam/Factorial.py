def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)


num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    sum_fact += fact(digit)
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
