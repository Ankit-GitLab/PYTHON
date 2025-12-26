class Account:
    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo = accountNo

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("total balance = ", self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount, "was credited")
        print("total balance = ", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(10000,896947)
acc1.debit(992)
acc1.credit(29)