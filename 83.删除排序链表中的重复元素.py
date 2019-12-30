#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next and head.val == head.next.val else head
        # t = head
        # p = head
        # while t:
        #     if t.val == p.val:
        #         t = t.next
        #     else:
        #         p.next = t
        #         p = t
        #         t = t.next
        # if p:
        #     p.next = None
        # return head

        
# @lc code=end

