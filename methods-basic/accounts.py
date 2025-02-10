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
        self._transaction_list = [Account._current_time(), balance]
        print(f"Account created for {self.name}")
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is deposited")
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))   
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn")
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f"Amount must be greater than zero and no more than your account balance")
        return self.balance
    
    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))




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
    aditi.show_transactions()

    steph = Account("Steph", 1000)
    steph.deposit(100)
    steph.withdraw(300)
    steph.show_transactions()


