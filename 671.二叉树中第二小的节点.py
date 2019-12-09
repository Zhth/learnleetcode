#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        first, second = root.val, -1
        stack = [root]
        while stack:
            t = stack.pop()
            for node in [t.left, t.right]:
                if node:
                    if node.val == first:
                        stack.append(node)
                    elif second == -1 or second > node.val:
                        second = node.val
        return second

                
# @lc code=end

