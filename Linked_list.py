class node:
    def __init__(self,value):
        self.head = None
        self.tail = None
class Sll:
    def __init__(self,value):
        self.value=value
        self.next = None
    def append(self,value):
        new_node= node(value)
        self.next = new_node
        self.tail = new_node









