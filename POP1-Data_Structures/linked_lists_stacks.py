"""
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # top stores a Node

    def push(self, x):
        # implement this: adds a new Node, makes top point to it,
        # old top is "saved in" the new Node's next

        if self.top == None:
            self.top = Node(x)
            self.top.next = None
        else:
            new_top = Node(x)
            new_top.next = self.top
            self.top = new_top

    def pop(self):
        # implement this: makes top point to the next of the Node pointed to by top
        self.top = self.top.next

    def peek(self):
        # implement this: returns the data of the Node pointed to by top
        return self.top.data

    def is_empty(self):
        # implement this: returns True if there are no Nodes in
        # Stack, otherwise False
        if self.top == None:
            return True
        else:
            return False


      
s = Stack()
s.push(1)
s.push(2)
s.peek() 
s.pop()
s.peek() 
s.is_empty()==False 
s.pop() 
s.is_empty()==True
"""


# Model Answer:
# -------------


class Node:
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
        return self.top is None
