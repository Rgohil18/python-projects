class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail = new_node
            self.next = new_node
    def prepend(self,value):
        new_node = node(value)
        if self.head is None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head = new_node
