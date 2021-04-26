# 13198061

"""
1 - Tuples are immutable and do not support item assignment.
You can cast to list and back to tuple e.g.

changed = list(t)
...
return tuple(changed)
 
2 - for loop starts at 1 but Python indexes from 0
The loop begins at 1 as per the range statement, but Python indexes from 0. This can be changed by the following code:

for i in range(0, len(t)):

Here the 1 was changed to 0 
"""