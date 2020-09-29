"""
def right_justify(string):
    padding = 70 - len(string)
    print ('-' * padding + string)

right_justify('monty')
"""

"""
def do_twice(func, arg):
    
    func: function object
    arg: argument passed to the function
    
    func(arg)   # Pass an argument to a specific function
    func(arg)

do_twice(print, 'fred')

"""
def print_beam():
    print('+'+'-'*4, end='')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_column():
    print('|' + ' '*4, end='')

def print_columns():
    do_twice(print_column)
    print('|')

def print_block():
    print_beams()
    do_four(print_columns)

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_grid():
    do_twice(print_block)
    print_beams()

print_grid()

