# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# def preOrderTraverse(root):
#     # print(root.val)
#     yield root.val
#     temp = root.left
#     stack = [root]
#     while stack:
#         while temp:
#             # print(temp.val)
#             yield root.val
#             stack.append(temp)
#             temp = temp.left
#         temp = stack.pop().right
#         if temp:
#             # print(temp.val)
#             yield root.val
#             stack.append(temp)
#             temp = temp.left

# def postOrderTraverse(root):
#     # print(root.val)
#     yield root.val
#     temp = root.right
#     stack = [root]
#     while stack:
#         while temp:
#             # print(temp.val)
#             yield root.val
#             stack.append(temp)
#             temp = temp.right
#         temp = stack.pop().left
#         if temp:
#             # print(temp.val)
#             yield root.val
#             stack.append(temp)
#             temp = temp.rightv



# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def preOrderTraverse(root):
#             # print(root.val)
#             yield root.val
#             temp = root.left
#             stack = [root]
#             while stack:
#                 while temp:
#                     # print(temp.val)
#                     yield root.val
#                     stack.append(temp)
#                     temp = temp.left
#                 temp = stack.pop().right
#                 if temp:
#                     # print(temp.val)
#                     yield root.val
#                     stack.append(temp)
#                     temp = temp.left

#         def postOrderTraverse(root):
#             # print(root.val)
#             yield root.val
#             temp = root.right
#             stack = [root]
#             while stack:
#                 while temp:
#                     # print(temp.val)
#                     yield root.val
#                     stack.append(temp)
#                     temp = temp.right
#                 temp = stack.pop().left
#                 if temp:
#                     # print(temp.val)
#                     yield root.val
#                     stack.append(temp)
#                     temp = temp.rightv
#         if root.left is None:
#             if root.right:
#                 return False
#             else:
#                 return True
#         yieldleft = preOrderTraverse(root.left)
#         yieldright = postOrderTraverse(root.right)
#         while True:
#             try:
#                 if next(yieldleft) == next(yieldright):
#                     continue
#                 else:
#                     return False
#             except:
#                 return True

class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.ismirror(root.left, root.right)
        
    def ismirror(self, left, right):
        if (not left) and (not right):
            return True
        else:
            try:
                if left.val == right.val:
                    return self.ismirror(left.left, right.right) and self.ismirror(left.right, right.left)
                else:
                    return False
            except:
                return False

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        try:
            if left.val == right.val:
                if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
                    return True
            return False
        except:
            return False