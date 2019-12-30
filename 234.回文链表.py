#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 反转链表，快慢指针,找到链表的中心位置，一个指针跟在慢指针后反转链表
        RHead = None
        if not head or not head.next:
            return True
        else:
            slow = head
            quick = head.next

        while quick and quick.next:
            temp = slow
            slow = slow.next
            quick = quick.next.next
            temp.next = RHead
            RHead = temp
        
        if quick:  # 偶数
            quick = slow.next
            slow.next = RHead
        else:
            quick = slow.next
            slow = RHead

        while quick and slow:
            if quick.val != slow.val:
                return False
            else:
                quick = quick.next
                slow = slow.next
        return True

# @lc code=end

