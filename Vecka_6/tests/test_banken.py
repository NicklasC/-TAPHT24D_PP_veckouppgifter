from Vecka_6.src.banken import Bank


def test_bank_balance_with_no_initial_deposit():
    bank = Bank()
    assert bank.balance() == 0


def test_bank_balance_with_initial_deposit():
    bank = Bank(100)
    assert bank.balance() == 100


def test_multiple_bank_deposits():
    bank = Bank()
    bank.deposit(100)
    bank.deposit(25)
    assert bank.balance() == 125


def test_valid_bank_withdrawal():
    bank = Bank(100)
    bank.withdraw(50)
    assert bank.balance() == 50


def test_invalid_bank_withdrawal():
    bank = Bank(100)
    bank.withdraw(150)
    assert bank.balance() == 100


def test_apply_interest():
    bank = Bank(100)
    bank.apply_interest(5)
    assert bank.balance() == 105


def test_can_i_pay_bill_true_expected():
    bank = Bank(100)
    assert bank.can_i_pay_bill(50) == True


def test_can_i_pay_bill_false_expected():
    bank = Bank(100)
    assert bank.can_i_pay_bill(150) == False
