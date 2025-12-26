def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR")

n = int(input("Enter a $ to converter in Rupess = "))
converter(n)