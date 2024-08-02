class employee:
    def __init__(self,name,time):
        self.name = name
        self.time = time
    def print(self):
        print(f"my name is {self.name},i have joined from last {self.time} days")
class person(employee):
    def __init__(self,gender):
        self.gender = gender
        print(f"my gender is {self.gender}")



x = employee("ravi",30)
x.print()
x = person("ravi")
y = employee("vijay",45)
y.print()

