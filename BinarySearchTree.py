# Create a binary search tree and find the amount of nodes to its max height (its largest amount of edges created)
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    # Create the binary search tree
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    # Find the max amount of edges made in binary search tree (essentially a depth-first search)
    def getHeight(self,root):
        if root.left and root.right:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        elif root.right and root.left == None:
            return 1 + self.getHeight(root.right)
        elif root.left and root.right == None:
            return 1 + self.getHeight(root.left)
        else:
            return 0
    # Prints every node by level (essentially a breadth-first search)
    def levelOrder(self, root):
        currentlevel = [root]
        while currentlevel:
            nextlevel = list()
            for node in currentlevel:
                print(node.data, end=' ')
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            currentlevel = nextlevel
    # Print the newly created and ordered binary tree
    def in_order_print(self,root):
        if not root:
            return
        self.in_order_print(root.left)
        print(root.data,end=' ')
        self.in_order_print(root.right)
    # Print the newly created and unordered binary tree
    def pre_order_print(self,root):
        if not root:
            return
        print(root.data,end=' ')
        self.pre_order_print(root.left)
        self.pre_order_print(root.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
#myTree.in_order_print(root)
myTree.levelOrder(root)
#print(height)