def add(num1: int, num2: int) -> int:
    return num1 + num2
  
def multiply(num1: int, num2: int) -> int:
    return num1 * num2

def divide(num1: int, num2: int) -> float:
    return num1 / num2

def substract(num1: int, num2: int) -> int:
    return num1 - num2
  
class InsufficientFunds(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance: int = 0):
        self.balance = starting_balance

    def deposit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int) -> int:
        if amount > self.balance:
           raise InsufficientFunds("Insufficient funds in account")
        self.balance -= amount
        return self.balance

    def check_balance(self) -> int:
        return self.balance
    
    def collect_interest(self) -> int:
        self.balance *= 1.1
        return self.balance