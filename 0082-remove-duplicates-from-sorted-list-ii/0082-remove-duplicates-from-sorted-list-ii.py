# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode()
        prev.next = head
        
        left = head
        right = left.next if left else None
        head = prev
        
        while left and right:
            
            duplicateFound = False
            
            while right and left.val == right.val:
                right = right.next
                duplicateFound = True

            if duplicateFound:
                prev.next = right
                left = right
                right = right.next if right else None

            else:
                prev = prev.next
                right = right.next
                left = left.next
        
        return head.next
        
        

            
        
        
        
        
        
        
            
            
                
                
        