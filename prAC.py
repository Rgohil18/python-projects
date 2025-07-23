class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Que():
    def __init__(self):
        self.head =None
        self.tail = None
    def first_element(self,value):
            first_node = node(value)
            self.head = first_node
            self.tail = first_node
    def Add_element(self,value):
        newnode = node(value)
        self.tail.next = newnode
        self.tail= newnode
    def removing(self):
        self.head=self.head.next
    def peek(self):
        return self.head.value


