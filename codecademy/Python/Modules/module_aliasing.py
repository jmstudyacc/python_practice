"""
Fortunately, this name can be altered by aliasing using the as keyword:

# import module_name as name_you_pick_for_the_module

Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything. 
This syntax is considered dangerous because it could pollute our local namespace. 
Pollution occurs when the same name could apply to two possible things. 
For example, if you happen to have a function floor() focused on floor tiles, 
using from math import * would also import a function floor() that rounds down floats.

Let’s combine your knowledge of the random library with another fun library called matplotlib, which allows you to plot your Python code in 2D. 

"""

#import codecademylib3_seaborn
from matplotlib import pyplot as plt     
import random

# Add your code below:
numbers_a = range(1, 13)                        # assigns the variable to a range of numbers
numbers_b = random.sample(range(1000), k = 12)  # assigns the var to 12 random numbers from 0-1000

plt.plot(numbers_a, numbers_b)    # Leveraging matplotlib to plot the numbers
plt.show()                        # matplotlib to show the graph