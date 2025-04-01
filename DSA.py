class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:  # ✅ FIXED: Check for None
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1  # ✅ FIXED: Update length


    def insert(self,index,value):
        new_node = Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        if index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1

    def traverse(self):
        current =self.head
        while current is not None:
            print(current.value)
            current=current.next

    def search(self,target):
        temp_node = self.head
        if temp_node.value!=target:
            temp_node=temp_node.next
            return True
        print(temp_node)
    def Get(self,index):
        temp_index = 0
        temp_value=self.head
        if temp_index!=index:
            temp_index=temp_index+1
            temp_value=temp_value.next
        return temp_value.value

    def Get2(self,index):
        current =self.head
        for _ in range(index):
            current = current.next
        return current.value
    def popfirst(self):

      if self.head!=None:
            pop_this = self.head
            self.head = self.head.next
            pop_this.next = None
            self.length = self.length-1
            return pop_this.value
      else:
          print("linkedlist is empty")
    def poplast(self):
        last_pop = self.tail
        temp =self.head
        while temp.next is not self.tail:
            temp = temp.next
        temp=self.tail
        temp.next=None
        self.length = self.length -1
    def all_nodes(self):
        temp1 = self.head
        temp2 = self.tail
        temp1.next = None
        temp2.next = None
        temp1.value = None
        temp2.value = None

    def remove(self,index):

        temp_node = self.head
        for _ in range(index):
            temp_node=temp_node.next
        temp_node2 = self.head

        for _ in range(index-1):
            temp_node2 = temp_node2.next
        temp_node2.next = temp_node.next
        temp_node.next = None
        return temp_node.value
    def deleteall(self):
        self.head=None
        self.tail=None
        self.length=0
 # ✅ Testing the Linked List
new_linked_list = Linkedlist()
new_linked_list.append(10)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.Get(2))
print(new_linked_list.popfirst())
print(new_linked_list.poplast())
print(new_linked_list)
print(new_linked_list.all_nodes())
print(new_linked_list)
print(new_linked_list.remove(0))

# import numpy as np




