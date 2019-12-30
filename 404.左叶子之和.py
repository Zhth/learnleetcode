#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp is None:
                continue
            if temp.left:
                if not temp.left.left and not temp.left.right:
                    sum += temp.left.val
                else:
                    stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return sum          
      
# @lc code=end

