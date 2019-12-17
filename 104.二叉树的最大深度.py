#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        t = [root]
        res = 1
        while True:
            tlist = []
            for node in t:
                for n in [node.left, node.right]:
                    if n:
                        tlist.append(n)
            if tlist:
                t = tlist
                res += 1
            else:
                return res


        
# @lc code=end

