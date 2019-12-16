#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            temp, head = l1, l1
            t1, t2 = l1.next, l2
        else:
            temp, head = l2, l2
            t1, t2 = l1, l2.next
        while t1 and t2:
            if t1.val < t2.val:
                temp.next = t1
                temp = temp.next
                t1 = t1.next
            else:
                temp.next = t2
                temp = temp.next
                t2 = t2.next
        if t1 is None:
            temp.next = t2
        else:
            temp.next = t1
        return head


        
# @lc code=end

