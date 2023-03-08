# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        merged = ListNode()
        
        
        curr1 = list1
        curr2 = list2
        currM = merged
        
#         while curr1 and curr2:
            
#             if curr1.val >= curr2.val:
#                 currM.next = ListNode(curr2.val)
#                 currM = currM.next
#                 curr2 = curr2.next
                
#             else:
#                 currM.next = ListNode(curr1.val)
#                 currM = currM.next
#                 curr1 = curr1.next
                
#         currM.next = curr1 if curr1 else curr2
        
#         return merged.next
    
    
        def recur(curr1, curr2, currM):
            
            if not curr1 and not curr2:
                return 
            
            if not curr1 and curr2:
                currM.next = curr2
                
                recur(curr1, curr2.next, currM.next)
                
            elif curr1 and not curr2:
                currM.next = curr1
                recur(curr1.next, curr2, currM.next)
                
            else:
                
                if curr1.val >= curr2.val:
                    currM.next = curr2
                    recur(curr1, curr2.next, currM.next)
                    
                else:
                    currM.next = curr1
                    recur(curr1.next, curr2, currM.next)
          
        recur(curr1, curr2, currM)
        
        return merged.next
                    
                



            
            
        
        
        
        
        