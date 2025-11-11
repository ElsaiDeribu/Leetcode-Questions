# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy
        curr = prev.next
        dup_found = False

        while curr and curr.next:
            if curr.val == curr.next.val:
                dup_found = True
                curr = curr.next
                

            else:
                if dup_found:
                    prev.next = curr.next
                    curr = prev.next if prev else None
                    dup_found = False
                else:
                    prev = curr
                    curr = curr.next

        if dup_found:
            prev.next = curr.next
            curr = prev.next if prev else None
            dup_found = False

        return dummy.next
            
        