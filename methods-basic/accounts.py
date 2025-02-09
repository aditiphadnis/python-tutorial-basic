

class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Account created for {self.name}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is deposited")
            self.show_balance()
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn")
            self.show_balance()

        else:
            print(f"Amount must be greater than zero and no more than your account balance")
        return self.balance
    
    def show_balance(self):
        print(f"Balance is {self.balance}")


if __name__ == "__main__":
    # Test the account class
    aditi = Account("Aditi", 0)
    aditi.deposit(1000)
    aditi.withdraw(500)
    # aditi.show_balance()
    aditi.withdraw(2000)
    # aditi.show_balance()
    aditi.deposit(2000)
    # aditi.show_balance()
    aditi.withdraw(2000)
    # aditi.show_balance()
