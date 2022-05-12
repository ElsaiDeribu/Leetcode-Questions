# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = head 
        i = head
        j = head.next
        
        while i.next: 
            while j:
                if j.val < i.val:
                    i.val, j.val = j.val, i.val
                    
                j = j.next
                    
            i = i.next
            j = i.next
            
        return newhead
    
 #         prev, j, i = None, head, head
        
#         while i:
#             while j.next:
                
#                 if j.next.val < i.val:
#                     temp = j.next
#                     # print(temp)
#                     j.next = j.next.next
#                     temp.next = i
#                     if prev:
#                         prev.next = temp
#                     i = temp
#                     if not prev:
#                         head = i
#                     j = i
                    
                     
#                 j = j.next
#             prev = i
#             i = i.next
#             j = i
            
#         return head
                    
            
