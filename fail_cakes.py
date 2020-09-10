dollars_cupcakes = int(input())
cents_cupcakes = int(input())
num_cupcakes = int(input())

dollar_sumcakes = dollars_cupcakes * num_cupcakes
cents_cupcakes = cents_cupcakes * num_cupcakes

monetary_cents = cents_cupcakes / 100
cents_to_dollars = monetary_cents // 1
remaining_cents = cents_cupcakes % 100


total_dollars = dollar_sumcakes + cents_to_dollars

print(int(total_dollars), int(remaining_cents))


"""
item_dollars = int(input())
item_cents = int(input())
n = int(input())
total_cents = (item_dollars * 100 + item_cents) * n
print(total_cents // 100, total_cents % 100)
"""
