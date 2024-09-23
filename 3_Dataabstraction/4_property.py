class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    @property
    def balance(self):
        # Getter for balance
        print('Getter-->Balance')
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        # Setter for balance with validation
        print('Setter-->Setting Balance')
        if amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance cannot be negative")
    
    def deposit(self, amount):
        self.balance += amount  # This uses the setter to update balance

    def withdraw(self, amount):
        if self._balance >= amount:
            self.balance -= amount  # This uses the setter to update balance
        else:
            raise ValueError("Insufficient funds")

# Creating an instance
account = BankAccount(1000)

# Accessing the balance using the getter
print("Initial Balance:", account.balance)

# Depositing and withdrawing
account.deposit(500)
print("Balance after deposit:", account.balance)

account.withdraw(300)
print("Balance after withdrawal:", account.balance)

# account.balance = -500  # Raises ValueError: Balance cannot be negative
