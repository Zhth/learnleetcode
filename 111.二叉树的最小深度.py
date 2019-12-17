#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        s = [root]
        res = 1
        while True:
            t = []
            for node in s:
                if node.left is None and node.right is None:
                    return res
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            s = t
            res += 1       
# @lc code=end

