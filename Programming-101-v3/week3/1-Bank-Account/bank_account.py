class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.initial_balance = balance
        self.currency = currency
        self.list_history = []
        self.list_history.append("Account was created")

    def balance(self):
        self.list_history.append(
            "Balance check -> {}{}".format(self.initial_balance, self.currency))
        return int(self.initial_balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        if self.initial_balance >= amount:
            self.initial_balance -= amount
            self.list_history.append(
                "{}{} was withdrawed".format(amount, self.currency))
            return True
        else:
            return False

    def deposit(self, amount):
        if amount < 0:
            raise ValueError

        self.initial_balance += amount
        self.list_history.append(
            "Deposited {}{}".format(self.initial_balance, self.currency))

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.initial_balance, self.currency)

    def __int__(self):
        self.list_history.append(
            "__int__ check -> {}{}".format(self.initial_balance, self.currency))
        return int(self.initial_balance)

    def transfer_to(self, account, amount):
        if amount < 0 or self.initial_balance <= amount or self.currency != account.currency:
            raise ValueError
        if self.currency == account.currency:
            self.initial_balance -= amount
            account.initial_balance += amount
            return True
        else:
            return False

    def history(self):
        return self.list_history


account = BankAccount("Rado", 0, "$")

print (account)
account.deposit(1000)
print (account.balance())
print (str(account))
print (int(account))
print (account.history())
print (account.withdraw(500))
print (account.history())
print (account.withdraw(1000))
print (account.balance())
print (account.history())

print (10 * '-')

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")

print (rado.transfer_to(ivo, 500))
print (rado.balance())
print (ivo.balance())
