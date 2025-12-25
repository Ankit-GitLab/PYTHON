num = int(input("Enter a number : "))

fact = 1

for val in range(1,num+1):
    fact *= val

print("Factorial = ",fact)