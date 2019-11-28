# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        stack = [[root]]
        result = []
        while stack:
            tempNode = stack.pop()
            result.append([node.val for node in tempNode])
            tempList = []
            for node in tempNode:
                if tempNode.left:
                    tempList.append(tempNode.left)
                if tempNode.right:
                    tempList.append(tempNode.right)
            if tempList:
                stack.append(tempList)
        result.reverse()
        return result
        