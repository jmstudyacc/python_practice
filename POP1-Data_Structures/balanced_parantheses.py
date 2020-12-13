"""
Attempt this problem after you solved the Linked Lists and Stacks
problem (Session 11 Problem 2).
This is because you can use your implementation of Stack to solve
this problem.

Given a string of parentheses of four types:
(), [], {} and <>,

print True if the parentheses of the string are balanced,
otherwise print False.
For the examples of balanced/unbalanced strings and
the algorithm to solve this problem using Stack,
see Session 11 lecture slides.

For example, on input:
([{}<>])
your output must be:
True
"""

"""
Logic:
------
- Set of accepted opening symbols
- Add accepted symbols onto stack via loop
- Check the symbols on stack compared to non-accepted symbols
- If symbol in string matches with symbol on stack, pop top symbol on stack
- Repeat until stack is empty
- If stack is empty return True 
"""
# importing Stack class from another file
from linked_lists_stacks import *

# need to uncomment this if not able to import
"""class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # top stores a Node

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        self.top = self.top.next

    def peek(self):
        return self.top.data

    def is_empty(self):
        return self.top == None
"""
# creating the function
def balan_paren(p_str):
    # defining the open symbols
    open_sym = "({[<"
    close_sym = ")}]>"
    s = Stack()
    for sym in p_str:
        # check if symbol is opening
        if sym in open_sym:
            s.push(sym)
        # check if symbol is closing
        else:
            # assigning value to track & hold value
            o_sym = s.top.data
            if sym in close_sym:
                # various conditionals to check correct open & closing tags
                if sym == ")" and o_sym == "(":
                    # if the symbols match the top value on stack is popped off
                    s.pop()
                elif sym == "}" and o_sym == "{":
                    s.pop()
                elif sym == "]" and o_sym == "[":
                    s.pop()
                elif sym == ">" and o_sym == "<":
                    s.pop()
            # if no matches, break as may be at empty stack
            else:
                break
    # s.is_empty() returns True then the stack is empty and therefore balanced
    if s.is_empty():
        return True
    else:
        return False

# receive input from user
symb_input = input()

print(balan_paren(symb_input))
# check the input using for loop

"""
MODEL ANSWER:
-------------

class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None    #top stores a Node
  def push(self, x):
    new_node = Node(x)
    new_node.next = self.top
    self.top = new_node
  def pop(self):
    self.top = self.top.next
  def peek(self):
    return self.top.data
  def is_empty(self):
    return self.top == None
    
stk = Stack()
s= input()
for sym in s:
  if sym in {"(", "[", "{", "<"}:
    stk.push(sym)
  else: #sym is a closing symbol
    sym1 = stk.peek()
    if (sym1 == "(" and sym == ")") or (sym1 == "[" and sym == "]") or \
    (sym1 == "{" and sym == "}") or (sym1 == "<" and sym == ">"): 
      stk.pop()
    else: 
      break
    
if stk.is_empty(): print("True")
else: print("False")
"""