class Counter:
    # provide __init__ to act as the constructor
    def __init__(self, my_id):
        self._items = {}
        self._id = my_id

    # provide a method to add a new entry to Counter
    def add(self, item_name, amount, price_of_unit):
        items = self._items
        # print(item_name, amount, price_of_unit)

        # checking to see if the item_name variable is in the dictionary
        if item_name in items:
            # if it is in the dictionary then do the following
            # print(f"\nThe amount for {item_name} currently stored is:  {items.get(item_name)[0]}")
            # print(f"The amount to be added to {item_name} is {amount}")
            # print(f"The result of this addition is: {items.get(item_name)[0] + amount}")
            updated_amount = items.get(item_name)[0] + amount
            updated_item = {item_name.title(): [updated_amount, float("%.2f" % price_of_unit)]}
            items.update(updated_item)
            # print(f"The new amount of {item_name} is: {updated_amount}")
        # create an entry in form of a dictionary and use provided values
        else:
            new_item = {item_name.title(): [int(amount), float("%.2f" % price_of_unit)]}
            # update the dictionary 'items' with the dictionary entry
            items.update(new_item)

        return items


    def reset(self):    def remove(self, item_name, amount):
        # method needs to remove an entry, requirements are hard to understand
        # test the removal first, translate the wording later :(
        items = self._items
        remove_item = item_name.title()
        # check if the word is present in the collection
        if remove_item in items:
            # 2 checks here, if amount passed is greater than amount in dict
            stored_amount = items.get(remove_item)[0]
            stored_price = items.get(remove_item)[1]
            #print(stored_price)
            if stored_amount <= amount:
                items.pop(remove_item)
                #print(f'**** {remove_item} WAS REMOVED FROM THIS COLLECTION ****')

            else:
                r_updated_amount = stored_amount - amount
                r_updated_item = {item_name.title(): [r_updated_amount, float("%.2f" % stored_price)]}
                items.update(r_updated_item)
                #print(f'**** {remove_item} HAD ITS QUANTITY CHANGED BY: {amount} ****')
        else:
            # Do nothing
            #print(f'**** {remove_item} IS MISSING FROM THIS COLLECTION ****')
            pass

        # erase all the previous information by reassigning as empty dict
        self._items.clear()

    def get_total(self):  # provides the running total of entries
        total_value = 0
        # can't index easily with dictionary so make it into a list to index
        item_list = list(self._items.items())
        for i in range(len(item_list)):
            item_name = item_list[i][1][0]
            price_of_unit = item_list[i][1][1]
            total_item_price = item_name * price_of_unit
            total_value += total_item_price

        return round(total_value, 2)

    def status(self):
        total_units = 0
        collection_id = self._id
        total_price = self.get_total()
        total_price = float(total_price)
        item_list = list(self._items.items())
        for item in range(len(item_list)):
            unit = item_list[item][1][0]
            total_units += unit

        return f'{collection_id} {total_units} {total_price}'


# testing the my_id portion of __init__ method
a = Counter('001')

# adding items to the dictionary created by __init__
a.add("Spaghetti", 5, 1.8)
a.add("Ice Cream", 2, 3.4)
a.add('Spaghetti', 3, 1.8)
a.add('Cake', 1, 4.5)
print(a.status())
print(a._items)
a.remove('cake', 1)
a.remove('ice cream', 4)
print(a._items)
print(a.status())
'''
a.add("bananas", 10, 0.8)
a.add('turkey', 1, 9.63)

# printing the result of get_total() to test arithmetic and format
print(a.get_total())


# testing & verifying remove() method
a.remove('turkey')
print(a.get_total())
a.add('turkey', 1, 9.63)

# testing & verifying reset() method
a.reset()
print(a.get_total())

# adding other items & verifying to confirm function after reset
a.add("ramen", 5, 1.8), a.add('porkchops', 6, 2.73)
print(a._items) # should not access class instance vars like this

# testing the get_status() method
print(a.status())

# checking remove() method after adding some conditional logic
a.remove('turkey')
print(a._items)
print(a.status())
a.remove('ramen')
print(a._items)
print(a.status())
'''
