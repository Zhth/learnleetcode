#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
        
# @lc code=end

