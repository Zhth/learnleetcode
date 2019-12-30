#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        rootH, rootB = self.HightandBalanced(root)
        return rootB    
    def HightandBalanced(self, root):
        if root is None:
            return 0, True
        leftH, leftB = self.HightandBalanced(root.left)
        rightH, rightB = self.HightandBalanced(root.right)
        if leftB == False or rightB == False:
            return max(leftH, rightH) + 1, False
        if abs(leftH - rightH) > 1:
            return max(leftH, rightH) + 1, False
        return max(leftH, rightH) + 1, True

# @lc code=end

