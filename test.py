class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(1)
print(a == b)
print(a is b)