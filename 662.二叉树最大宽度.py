#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        lenth = 0
        while stack:
            lenth = max(stack[-1][1] - stack[0][1], lenth)
            temp = []
            for node, num in stack:
                for i, t in enumerate((node.left, node.right)):
                    if t:
                        temp.append((t, 2*num + i))
            stack = temp
        return lenth + 1
       
# @lc code=end

