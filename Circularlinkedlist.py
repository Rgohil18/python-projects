class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
        self.length += 1

    def __str__(self):
        if self.head is None:
            return "Circular Linked List is empty"

        temp_node = self.head
        result = ''
        while True:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result + " (circular)"
    def prepend(self,value):
        prepend = Node(value)
        prepend.next = self.head
        self.head = prepend
        self.tail.next = prepend
        self.length = +1
    def insert(self,index,value):
        temp_node = self.head
        new_node = Node(value)
        for _ in range(index-1):
            temp_node.next = new_node
        new_node.next = temp_node.next
        pass
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node ==self.head:
                break
    def search(self,value):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value==value:
                print("yes")
            temp_node = temp_node.next

            if temp_node == self.head:
                break
        return False

    def get(self,index):
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
            print(temp_node.value)






first = CSLinkedList(10)
first.append(20)
first.append(30)
print(first)
first.prepend(0)
print(first)
first.traverse()
first.search(30)
first.get(0)
