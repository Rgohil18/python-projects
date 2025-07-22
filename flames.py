class stack :
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return "the stack is empty"
        else:
            return "the stack is not empty"

    def push(self,value):
        self.list.append(value)

    def pop(self):
        self.list.pop()
        return self.list
    def peek(self):
        return self.list[len(self.list)-1]

stack1 = stack()
stack1.push(10)
print(stack1)
stack1.push(20)
print(stack1)
print(stack1.pop())
print(stack1)
stack1.push(30)
print(stack1)
print(stack1.peek())

