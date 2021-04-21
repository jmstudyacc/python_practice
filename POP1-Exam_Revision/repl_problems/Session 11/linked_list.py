# creates the data structure that is a node
class Node:
    # this node is created by passing data
    def __init__(self, data):
        # data of the node is passed to self.data
        self.data = data

        # node is not created with a next
        self.next = None

    def __str__(self):
        return f"{self.data}"


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        # need to create a new node
        new_node = Node(x)

        # tell the new node your next node is what was top
        new_node.next = self.top

        # set top to equal the new_node
        self.top = new_node

    def pop(self):
        self.top = self.top.next

    def peek(self):
        return self.top

    def is_empty(self):
        return self.top is None


s1 = Stack()
s1.push(1)
s1.push(2)
print(s1.peek())
s1.pop()
print(s1.peek())
print(s1.is_empty())
s1.pop()
print(s1.is_empty())