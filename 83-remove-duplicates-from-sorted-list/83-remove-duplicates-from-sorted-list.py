# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        temp = head
    
        if temp == None:    
            return temp
        
        
        while temp and temp.next:
            if temp.val == temp.next.val and temp.next.next == None:
                temp.next = None
                break
            while temp.next and  temp.val == temp.next.val:
                nodeToDelete = temp.next
                temp.next = temp.next.next
                nodeToDelete.next = None
            
            temp = temp.next

        return ans