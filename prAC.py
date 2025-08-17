#class tree:
 #   def __init__(self,data,child = []):
  #      self.data = data
    #    self.child = child
   # def __str__(self, level=0):
     #   ret = "   " * level + str(self.data) + "\n"
      #  for child1 in self.child:
       #     ret += child1.__str__(level + 1)
       # return ret
    #def addchild(self,value):
     #   self.child.append(value)
class tree:
    def __init__(self, data, child=None):
        self.data = data
        # Create a new list every time if no child list is provided
        self.child = child if child is not None else []

    def __str__(self, level=0):
        ret = "   " * level + str(self.data) + "\n"
        for child1 in self.child:
            ret += child1.__str__(level + 1)
        return ret

    def addchild(self, value):
        self.child.append(value)


food = tree("food")
veg = tree("veg")
nonveg = tree("nonveg")

food.addchild(veg)
food.addchild(nonveg)

# Optional: children of veg
veg.addchild(tree("carrot"))
veg.addchild(tree("spinach"))

print(food)
