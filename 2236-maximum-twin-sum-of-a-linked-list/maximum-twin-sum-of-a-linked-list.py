# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast, slow = head, head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next


        prev = None
        curr = slow

        while curr:
           curr.next, prev, curr = prev, curr, curr.next


        ans = 0
        while prev:
            ans = max(head.val + prev.val, ans)
            prev, head = prev.next, head.next

        return ans
        


        