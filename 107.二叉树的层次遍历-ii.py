#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
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
                if node.left:
                    tempList.append(node.left)
                if node.right:
                    tempList.append(node.right)
            if tempList:
                stack.append(tempList)
        result.reverse()
        return result
        
# @lc code=end

