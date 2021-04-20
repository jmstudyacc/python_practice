class Counter:
    def __init__(self, my_id):
        # id is a string
        # _items is a dictionary, keys = string, values = list
        self._items = {}
        self._id = my_id

    def add(self, item_name, amount, price_of_unit):
        # if the entry does not yet exist add it with this shorthand entry operation
        if item_name not in self._items:
            self._items[item_name] = [amount, price_of_unit]

        elif price_of_unit <= 0 or amount <= 0:
            return ValueError(f"The {price_of_unit} or {amount} must be greater than 0.")

        else:
            # just add the new amount to the previous item - minimise required operations on dictionary
            self._items.get(item_name)[0] += amount

    def remove(self, item_name, amount):
        # if item_name is not present, do nothing
        if item_name not in self._items:
            pass
        else:
            # if the amount to remove is gte
            if amount >= self._items.get(item_name)[0]:
                self._items.pop(item_name)
            else:
                self._items.get(item_name)[0] -= amount

    def reset(self):
        self._items = {}

    def get_total(self):
        # returns float number representing the total price - rounded to 2nd fractional digit
        # use standard, round(x, 2) function
        total = 0
        for i in self._items:
            total += self._items[i][0] * self._items[i][1]

        return round(total, 2)

    def status(self):
        # returns string 'ID N M'
        # ID = id of counter, N = total amount, M = total price
        # round M to the 2nd fractional digit
        quantity = 0
        for i in self._items:
            quantity += self._items[i][0]

        return f"{self._id} {quantity} {self.get_total()}"


c = Counter("C001")
c.add("Spaghetti", 5, 1.8)
assert c.status() == "C001 5 9.0"
c.add("Ice Cream", 2, 3.4)
assert c.status() == "C001 7 15.8"
assert c.get_total() == 15.8
c.add("Spaghetti", 3, 1.8)
assert c.status() == "C001 10 21.2"
c.remove("Ice Cream", 1)
assert c.status() == "C001 9 17.8"
c.reset()
c.add("Coke", 5, 1.45)
assert c.status() == "C001 5 7.25"

