#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [[root]]
        res = []
        while stack:
            tlist = []
            t = stack.pop()
            n, s = 0, 0
            for node in t:
                n += 1
                s += node.val
                if node.left:
                    tlist.append(node.left)
                if node.right:
                    tlist.append(node.right)
            if tlist:
                stack.append(tlist)
            res.append(s/n)
        return res
            
# @lc code=end

