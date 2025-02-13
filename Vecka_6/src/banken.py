class Bank:
    def __init__(self, amount=0):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount

    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount

    def apply_interest(self, interest_rate):
        self.__balance *= (100 + interest_rate) / 100

    def can_i_pay_bill(self, amount):
        return amount <= self.__balance
