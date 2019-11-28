# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         temppre = None
#         temp = head
#         while temp:
#             tempnext = temp.next
#             temp.next = temppre
#             temppre = temp
#             temp = tempnext
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        