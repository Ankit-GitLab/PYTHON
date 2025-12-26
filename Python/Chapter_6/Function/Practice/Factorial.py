def cal_fact(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

n = int(input("Enter number : "))
print(cal_fact(n))