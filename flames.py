class basic:
    def __init__(self,name,gender):
        self.name = name
        self.gender= gender
        print(f"my name is {self.name}"
              f" i am {gender}")

class details(basic):
    def physical_measure(self,height,weight):
        print(f"my height is {height},my weight is {weight}")

class class_details(details):
    def __init__(self,class1,div):
        print(f"i am studying in class{class1}, division {div}")
        super(basic).__init__()
        super().physical_measure()


x = basic("ravi","male")
x = details()
x.physical_measure("5'7","54")
x = class_details("12th","h")


