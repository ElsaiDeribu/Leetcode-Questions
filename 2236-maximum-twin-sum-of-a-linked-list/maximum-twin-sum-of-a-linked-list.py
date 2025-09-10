# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ans = 0

        while prev:
            ans = max(head.val + prev.val, ans)
            prev = prev.next
            head = head.next


        return ans
        


        