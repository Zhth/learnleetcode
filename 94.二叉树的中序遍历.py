#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     self.appendRes(res, root)
    #     return res
    # def appendRes(self, res, root):
    #     if root is None:
    #         return res
    #     if root.left:
    #         self.appendRes(res, root.left)
    #     res.append(root.val)
    #     self.appendRes(res, root.right)
    #     return
        res = []
        visited = []
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp is None:
                continue
            if temp.left is None or temp.left in visited:
                res.append(temp.val)
                visited.append(temp)
                if temp.right:
                    stack.append(temp.right)
            else:
                stack.append(temp)
                stack.append(temp.left)
        return res


        
# @lc code=end

