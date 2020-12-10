
def add(item_name, amount, price):
    e = {item_name.title(): [int(amount), float("%.2f" % price)]}
    collection.update(e)


def get_total(c):
    total_value = 0
    # Used to get the running total of the 'shopping list' prices
    c_list = list(collection.items())
    for prices in range(len(c)):
        unit = c_list[prices][1][0]
        price = c_list[prices][1][1]
        unit_value = unit * price
        total_value += unit_value

    return total_value


# status function wants to print out the class ID, number of items & total price
def get_status(c):
    total_products = 0
    c_list = list(collection.items())
    # iterating over the dictionary and indexing in to get the required values
    for item in range(len(c)):
        unit = c_list[item][1][0]
        # key = c_list[item][0]
        total_products += unit

    return collection_id, total_products, '{:.2f}'.format(get_total(collection))


def reset(c):
    collection = {}
    return collection


def remove(self, item_name, amount):
    items = self._items

    if item_name in items:
        # 2 checks here, if amount passed is greater than amount in dict
        stored_amount = items.get(item_name)[0]
        if stored_amount <= amount:
            items.pop(remove_item)
        else:
            r_updated_amount = stored_amount - amount
            r_updated_item = {item_name.title(): [r_updated_amount, float("%.2f" % price_of_unit)]}
            items.update(r_updated_item)
    else:
        pass

    # class version accepts, (self, item_name, amount)
    # DONE if the item_name is not among the items previously added, do nothing;
    # if the item_name is among them but the amount is greater or equal to the number of previously added items
    # with this name, remove the record associated with item_name;
    # if the item_name is among them but the amount is less than the
    # number of previously added items with this name, subtract the former quantity from the latter
    # see the examples of use in the instructions (right pane)


collection = {}
collection_id = '001'
add("Spaghetti", 5, 1.8)
add("Chickens", 3, 2.7)
add("bananas", 10, 0.8)
print(collection)
print(get_status(collection))
print("**************")
print('\n', reset(collection))

# print(f'\nThe total value of purchased items is {total_value:.2f}.')
# print(f'The total quantity of items purchased is {products}.')
