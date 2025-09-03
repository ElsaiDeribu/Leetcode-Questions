# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head
        slow = head
        fast = head

        while fast and fast.next:

            prev = slow
            fast = fast.next.next
            slow = slow.next

        if prev.next:
            prev.next = prev.next.next

        else:
            return None

        return head



        