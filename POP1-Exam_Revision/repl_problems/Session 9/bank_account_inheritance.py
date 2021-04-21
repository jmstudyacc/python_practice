class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None

    def set_address(self, addr):
        self.address = addr


# BankAccount class has been created to eliminate redundancy in later account types
class BankAccount:
    def __init__(self, sort_code, account_number):
        self.sc = sort_code
        self.an = account_number

    def set_sort_code(self, sort_code):
        self.sc = sort_code

    def get_sort_code(self):
        return self.sc

    def set_account_number(self, account_number):
        self.an = account_number

    def get_account_number(self):
        return self.an

    def get_account_data(self):
        return f"{self.sc} {self.an}"


class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        # super() references the extension class and you then use __init__ with the params to populate
        super().__init__(sort_code, account_number)
        self.owner = owner

    def get_account_data(self):
        return f"{self.owner.first_name} {self.owner.last_name} {self.sc} {self.an}"


class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        self.owners = owners

    def get_account_data(self):
        return f"{self.owners[0].first_name} {self.owners[0].last_name}, {self.owners[1].first_name} {self.owners[1].last_name}, {self.sc} {self.an}"


john01 = Person("John", "Doe")
john01.set_address("Place")
john01_account = IndividualBankAccount("12-34-56", "12345678", john01)
# Check successful generation
assert john01_account.get_account_data() == "John Doe 12-34-56 12345678"

# Check getters & setters
john01_account.set_sort_code("22-24-26")
assert john01_account.get_sort_code() == "22-24-26"
john01_account.set_account_number("87654321")
assert john01_account.get_account_number() == "87654321"

mary01 = Person("Mary", "Ann")
mary01.set_address("Other place")
mary01_account = IndividualBankAccount("87-65-43", "98765432", mary01)

# Check mary01 account methods
assert mary01_account.get_account_data() == "Mary Ann 87-65-43 98765432"

acc02 = SharedBankAccount("11-22-33", "51015200", [mary01, john01])
# Check shared account details
assert acc02.get_account_data() == "Mary Ann, John Doe, 11-22-33 51015200"
