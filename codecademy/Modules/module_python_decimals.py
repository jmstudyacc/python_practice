"""
Being familiar with rounding errors in floating-point arithmetic 
you want to use a data type that performs decimal arithmetic more accurately. 
You could do the following:

# from decimal import Decimal
 
# cost_of_gum = Decimal('0.10')
# cost_of_gumdrop = Decimal('0.35')
 
# cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

Above, we use the decimal module’s Decimal data type to add 0.10 with 0.35. Since we used the Decimal type the arithmetic acts much more as expected.

Usually, modules will provide functions or data types that we can then use to solve a general problem, 
allowing us more time to focus on the software that we are building to solve a more specific problem.

Ready, set, fix some floating point math by using decimals!

"""

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)