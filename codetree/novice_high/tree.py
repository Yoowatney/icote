class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def inorder(self):
        traversal = []
        traversal.append(self.value)
        if self.left:
            traversal += self.left.inorder()
        if self.right:
            traversal += self.right.inorder()
        return traversal

    # def insert(self, x):
    #     node = self.root
    #     parent = self.root
    #     while node:
    #         parent  = node
    #         if node.value > x:
    #             node = node.left
    #         else:
    #             node = node.right
    #     if not parent:
    #         BST.root = Node(x)
    #     elif parent.value > x:
    #         parent.left = Node(x)
    #     else:
    #         parent.right = Node(x)
    #     pass

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, x):
        # if self.root:
        #     self.root.insert(x)
        #     pass
        # else:
        #     self.root = Node(x)
            # return
        node = self.root
        parent = self.root
        while node:
            parent  = node
            if node.value > x:
                node = node.left
            else:
                node = node.right
        if not parent:
            BST.root = Node(x)
        elif parent.value > x:
            parent.left = Node(x)
        else:
            parent.right = Node(x)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

bst = BST(Node(4))
bst.insert(5)
bst.insert(1)
bst.insert(2)
bst.insert(7)


print(bst.inorder())
