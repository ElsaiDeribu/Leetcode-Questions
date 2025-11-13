# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = prev = ListNode(0, head)


        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = curr.next.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next



