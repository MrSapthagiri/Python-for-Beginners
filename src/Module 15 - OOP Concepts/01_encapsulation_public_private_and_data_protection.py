# Module 15: OOP Concepts
# Topic 1: Encapsulation, public/private members, and data protection


# Example 1: Public attributes are directly accessible.
class PublicAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


account = PublicAccount("Asha", 100)
print("Example 1 - Balance:", account.balance)


# Example 2: A leading underscore marks a protected implementation detail.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient balance")
        self._balance -= amount

    def get_balance(self):
        return self._balance


savings = BankAccount("Asha", 500)
savings.deposit(100)
print("Example 2 - Balance:", savings.get_balance())


# Example 3: A getter provides read-only public access to protected data.
print("Example 3 - Getter:", savings.get_balance())


# Example 4: A method validates a withdrawal.
try:
    savings.withdraw(1000)
except ValueError as error:
    print("Example 4 -", error)


# Example 5: A property can expose a validated attribute-like interface.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("temperature is below absolute zero")
        self._celsius = value


temperature = Temperature(25)
print("Example 5 - Celsius:", temperature.celsius)


# Example 6: The property setter validates new values.
try:
    temperature.celsius = -300
except ValueError as error:
    print("Example 6 -", error)


# Example 7: Double underscores trigger name mangling.
class PasswordVault:
    def __init__(self, password):
        self.__password = password

    def verify(self, password):
        return password == self.__password


vault = PasswordVault("secret")
print("Example 7 - Password match:", vault.verify("secret"))


# Example 8: Name mangling is not absolute security and can be inspected.
print("Example 8 - Mangled name exists:",
      "_PasswordVault__password" in vault.__dict__)


# Example 9: Encapsulation keeps rules close to the object's data.
savings.withdraw(50)
print("Example 9 - Balance:", savings.get_balance())


# Example 10: Public methods form the object's supported interface.
print("Example 10 - Public methods:",
      hasattr(savings, "deposit"), hasattr(savings, "withdraw"))


# Quick review:
# - Public names have no leading underscore.
# - _name is a protected implementation convention.
# - __name is mangled and not truly private.
# - Methods and properties can validate and control access.
