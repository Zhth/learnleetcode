#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        tempNode = head
        if m == 1:
            p1end = None
            p2begin = head
        else:
            for _ in range(m - 2):
                tempNode = tempNode.next
            p1end = tempNode
            p2begin = tempNode.next
        t = p2begin
        p = p2begin.next
        for _ in range(n - m):
            p.next, t, p = t, p, p.next
        if p1end is None:
            p2begin.next = p
            return t
        p1end.next = t
        p2begin.next = p
        return head
     
# @lc code=end

