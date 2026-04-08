class bankaccount:
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("not sufficient balance ")
        else:
            self.balance = self.balance - amount
            print("take your cash",amount)
    def show_balance(self):
        print(self.balance)

account1 =bankaccount("Ganesh", 5000)
account1.show_balance()
account1.deposit(12000)
account1.show_balance()
account1.withdraw(3000)
account1.show_balance()
account1.withdraw(2300)
account1.show_balance()
account1.withdraw(12000)
