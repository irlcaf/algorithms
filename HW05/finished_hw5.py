# coding=UTF-8
import numpy as np

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else: 
            root.right =  self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        
        return root
            
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        y.height = 1 + max(self.getHeight(y.right), self.getHeight(y.left)) 
        x.height = 1 + max(self.getHeight(x.right), self.getHeight(x.left))

        return y
    
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.right), self.getHeight(y.left)) 
        x.height = 1 + max(self.getHeight(x.right), self.getHeight(x.left))

        return x

    def getHeight(self,root):
        if not root:
            return 0
        return root.height

    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        print("{0} ".format(root.val))
        self.inOrder(root.right)

if __name__ == "__main__":
    f = open('./05_input.in', 'r')
    lines = f.readlines()
    for line in lines:
        npyArray = np.fromstring(line, dtype=int, sep=',')
        # Write your code here
        tree = AVL_Tree()
        root = None
        for element in npyArray:
            root = tree.insert(root, element)
        tree.inOrder(root)
    



