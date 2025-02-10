import datetime
import pytz

class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_list = []  # Initialize as an empty list
        if balance > 0:
            self.transaction_list.append((self._current_time(), balance))
        print(f"Account created for {self.name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is deposited")
            self.show_balance()
            self.transaction_list.append((self._current_time(), amount))   
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn")
            self.show_balance()
            self.transaction_list.append((self._current_time(), -amount))
        else:
            print("Amount must be greater than zero and no more than your account balance")
        return self.balance
    
    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            tran_type = "deposited" if amount > 0 else "withdrawn"
            print("{:6} {} on {} (local time was {})".format(abs(amount), tran_type, date, date.astimezone()))


if __name__ == "__main__":
    # Test the account class
    aditi = Account("Aditi", 0)
    aditi.deposit(1000)
    aditi.withdraw(500)
    aditi.withdraw(2000)  # Should not allow
    aditi.deposit(2000)
    aditi.withdraw(2000)
    aditi.show_transactions()

    steph = Account("Steph", 1000)
    steph.deposit(100)
    steph.withdraw(300)
    steph.show_transactions()
