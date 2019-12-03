#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            NodeFast = head.next.next
            NodeSlow = head.next

            while NodeFast != NodeSlow:
                NodeFast = NodeFast.next.next
                NodeSlow = NodeSlow.next
        except:
            return None
        NodeFast = head
        while NodeFast != NodeSlow:
            NodeFast = NodeFast.next
            NodeSlow = NodeSlow.next
        return NodeSlow        
        
# @lc code=end

