class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def preordertraverse(self,rootnode):
        if not rootnode:
            return
        print(rootnode.data)
        self.preordertraverse(rootnode.left)
        self.preordertraverse(rootnode.right)
        # create nodes
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)

# call the traversal
root.preordertraverse(root)


