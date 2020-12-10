class Person:
    '''to handle person's details'''

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None  # addresses stored by strings

    def set_address(self, adr):
        self.address = adr  # strings


class BankAccount:
    def __init__(self, sort_code, account_number):
        '''TD implement this; creates a bank account
        with sort code as string and account number as string'''
        self.sc = sort_code
        self.an = account_number

    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sc = sort_code

    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sc

    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.an = account_number

    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.an

    def get_account_data(self):
        '''TD implement this; returns string "SC AN"
    where SC is sort code, AN is account number'''
        return f'{self.sc} {self.an}'


class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
        TD implement setting up an owner as Person'''
        self.own = owner

    def get_account_data(self):
        '''TD implement this; returns string "FN LN SC AN"
        where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        return f'{self.own.first_name} {self.own.last_name} {self.sc} {self.an}'


class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
    TD implement setting up an owners as a list of Persons'''
        self.owns = owners

    def get_account_data(self):
        '''TD implement this; returns string
        "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
        where FNi LNi is the i-th owner first and last names,
        SC is sort code, AN is account number'''
        return (
            f'{self.owns[0].first_name} {self.owns[0].last_name}, {self.owns[1].first_name} {self.owns[1].last_name}, '
            f'{self.sc} {self.an}')


"""
john01 = Person("John", "Doe")
john01.set_address("Birkbeck, Malet st., WC1E 7HX")
john01s_account = IndividualBankAccount("12-34-56", "12345678", john01)
#Test1 checks john01s_account.get_account_data()=="John Doe 12-34-56 12345678"
john01s_account.set_sort_code("11-11-11")
#Test2 check john01s_account.get_sort_code()=="11-11-11"


mary01 = Person("Mary", "Ann")
mary01.set_address("UCL, Gower st., WC1E 6BT")
mary01s_account = IndividualBankAccount("65-43-21", "87654321", mary01)
#Test3 checks mary01s_account.get_account_data()=="Mary Ann 65-43-21 87654321"
mary01s_account.set_account_number("99999999")
#Test4 checks mary01s_account.get_account_number()=="99999999"


acc02 = SharedBankAccount("11-22-33", "11223344", [john01, mary01])
#Test5 checks acc02.get_account_data()=="John Doe, Mary Ann, 11-22-33 11223344"
"""