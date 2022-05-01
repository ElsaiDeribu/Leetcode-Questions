# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        values = []
        
        temp = head
        
        while temp:
            values.append(temp.val)
            temp = temp.next
            
        temp = head 
        
        for i in range (len(values)-1,-1,-1):
            
            temp.val = values[i]
            
            temp = temp.next
            
        return head
            
        