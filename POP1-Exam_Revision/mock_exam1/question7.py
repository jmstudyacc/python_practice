class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def get_info(self):
        return f"{self.f_name} {self.l_name}"

    def get_name(self):
        return self.f_name, self.l_name


class Adult(Person):
    def __init__(self, f_name, l_name, phone):
        Person.__init__(self, f_name, l_name)
        self.phone = phone

    def get_phone(self):
        return f"{self.phone}"


class Child(Person):
    def __init__(self, f_name, l_name, p1, p2):
        Person.__init__(self, f_name, l_name)
        self.p1 = p1
        self.p2 = p2

    def get_info(self):
        return f"{self.f_name} {self.l_name} {self.p1.get_info()} {self.p2.get_info()}"

    def get_parents(self):
        return self.p1, self.p2



p = Person("Mary", "Ann")
print(p.f_name, p.l_name)
a = Adult("John", "Doe", "1234567")
assert a.get_info() == "John Doe"
print(a.f_name, a.l_name, a.phone)
c = Child("Richard", "Doe", p, a)
#print(c.get_info())
assert c.get_info() == "Richard Doe Mary Ann John Doe"
#print(str(c.get_parents()))
assert c.get_parents() == (p, a)