#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None and root.val == sum:
            return [[root.val]]
        leftList = self.pathSum(root.left, sum - root.val)
        rightList = self.pathSum(root.right, sum - root.val)
        tempList = []
        if leftList:
            for pathList in leftList:
                pathList.insert(0, root.val)
                tempList.append(pathList)
        if rightList:
            for pathList in rightList:
                pathList.insert(0, root.val)
                tempList.append(pathList)
        return tempList

    # def addList(self, root, List):
    #     if root is None:
    #         return False
    #     if root.left is None and root.right is None and root.val == sum:
    #         return True
    #     return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
# @lc code=end

