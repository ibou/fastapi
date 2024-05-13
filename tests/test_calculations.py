import pytest
from app.calculations import add, BankAccount, divide, InsufficientFunds, multiply, substract

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def hundred_bank_account():
    return BankAccount(100)


@pytest.mark.parametrize("num1,num2,expected", [
  (1, 2, 3),
  (0, 0, 0),
  (-1, -1, -2),
  (-1, 1, 0),
  (1, -1, 0),
  (1, 0, 1),
  (0, 1, 1),
  (0, -1, -1),
  (-1, 0, -1),
])

def test_add(num1, num2, expected):
  assert add(num1, num2) == expected

def test_multiply():
  assert multiply(1, 2) == 2
  assert multiply(0, 0) == 0
  assert multiply(-1, -1) == 1
  assert multiply(-1, 1) == -1
  assert multiply(1, -1) == -1
  assert multiply(1, 0) == 0
  assert multiply(0, 1) == 0
  assert multiply(0, -1) == 0
  assert multiply(-1, 0) == 0

def test_divide():
  assert divide(1, 2) == 0.5
  assert divide(-1, -1) == 1
  assert divide(-1, 1) == -1
  assert divide(1, -1) == -1
  assert divide(0, 1) == 0
  assert divide(0, -1) == -0.0

def test_substract():
  assert substract(1, 2) == -1
  assert substract(0, 0) == 0
  assert substract(-1, -1) == 0
  assert substract(-1, 1) == -2
  assert substract(1, -1) == 2
  assert substract(1, 0) == 1
  assert substract(0, 1) == -1
  assert substract(0, -1) == 1
  assert substract(-1, 0) == -1

def test_bank_set_initial_amount():
  account = BankAccount(100)
  assert account.check_balance() == 100

def test_bank_set_initial_amount_default(zero_bank_account): 
  assert zero_bank_account.balance == 0

def test_bank_deposit(hundred_bank_account):
    assert hundred_bank_account.deposit(100) == 200
    assert hundred_bank_account.deposit(100) == 300
    assert hundred_bank_account.deposit(100) == 400


def test_bank_withdraw(hundred_bank_account): 
    assert hundred_bank_account.withdraw(25) ==  75
    assert hundred_bank_account.withdraw(25) ==  50
    assert hundred_bank_account.withdraw(45) ==  5
    
    
def test_bank_insufficient_funds(hundred_bank_account):
    with pytest.raises(InsufficientFunds):
        hundred_bank_account.withdraw(101) 
    
    


def test_bank_collect_interest(hundred_bank_account):
    hundred_bank_account.collect_interest()
    assert round(hundred_bank_account.check_balance(), 6) == 110

@pytest.mark.parametrize('deposited, withdraw, expected', [
    (100, 50, 50),
    (100, 25, 75),
    (100, 100, 0),
    (100, 0, 100),
    (0, 0, 0),
    (-100, -100, 0),
])

def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.check_balance() == expected
    
