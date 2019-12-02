#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        lastvisited = root
        while stack:
            tempNode = stack.pop()
            if lastvisited == tempNode.right or lastvisited == tempNode.left:
                res.append(tempNode.val)
                lastvisited = tempNode
            elif tempNode.left is None and tempNode.right is None:
                res.append(tempNode.val)
                lastvisited = tempNode
            else:
                stack.append(tempNode)
                if tempNode.right:
                    stack.append(tempNode.right)
                if tempNode.left:
                    stack.append(tempNode.left)
        return res
    #     res = []
    #     self.postorderCur(res, root)
    #     return res
    def postorderCur(self, res, root):
        if root is None:
            return
        self.postorderCur(res, root.left)
        self.postorderCur(res, root.right)
        res.append(root.val)
        return


# @lc code=end
