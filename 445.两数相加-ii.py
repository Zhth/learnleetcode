#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res1, res2 = 0, 0
        t1, t2 = l1, l2
        while t1:
            res1 = 10*res1 + t1.val
            t1 = t1.next
        while t2:
            res2 = 10*res2 + t2.val
            t2 = t2.next
        res = str(res1 + res2)
        head = ListNode(res[0])
        t = head
        for i in range(1, len(res)):
            t.next = ListNode(res[i])
            t = t.next
        return head
        
# @lc code=end

