class employee:
    def __init__(self,name,time):
        self.name = name
        self.time = time
        print(f"my name is {self.name}, i have joined the company from last {self.time}"
              )
    def age(self,age):
        self.age = age
        print(f"my age is {self.age}")

class person(employee):
    def __init__(self,gender):
        self.gender = gender
        print(f"my gender is {self.gender}")

class place(person):
    def __init__(self,place):
        self.place=place
        print(f"i live in {self.place}")

def add(a,b):
        print(a+b)

x = place("mumbai")
x.age(18)
x = employee("ravi",30)
x = person("male")
x = add(1,2)




