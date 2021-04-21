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

    # function to print the stack contents - takes the 'top' node as the parameter
    def p_stack(self, top):

        # base condition to check if the stack is empty
        if top is None:
            return None

        elif top.next is None:
            # if the next node field for the 'top' node is None you have reached the end of the recursion
            # pass the value of the 'top' node for return
            return [top.data]

        else:
            # stack is assigned the value of top node's data
            stack = [top.data]

            # s_next is set to use the next node assigned to the current 'top' node
            s_next = top.next

            # print the contents of the stack
            print(stack, end=" ")

            # recursively call the method until base condition is met
            return self.p_stack(s_next)


s1 = Stack()
s_print = s1.p_stack(s1.peek())
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(5)
s1.push(6)
s_print = s1.p_stack(s1.peek())
print(s_print)
s1.pop()
print(s1.p_stack(s1.peek()))
s1.pop()
print(s1.p_stack(s1.peek()))
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print(s1.p_stack(s1.peek()))
s1.pop()
print(s1.p_stack(s1.peek()))
"""print(s1.peek())
s1.pop()
print(s1.peek())
print(s1.is_empty())
s1.pop()
print(s1.is_empty())"""
