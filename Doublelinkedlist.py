class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self,value):
        self.head = head
        self.tail = tail
    def __str__(self):

        return f"{self.prev}<--{self.value}-->{self.next}"

    def append(self,value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        new_node.next = None
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head=new_node





node = Node(10)
print(node)

