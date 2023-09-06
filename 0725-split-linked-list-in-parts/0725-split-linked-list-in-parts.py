# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = 0
        curr = head 
        
        while curr:
            count += 1
            curr = curr.next
            
            
        partSize = count // k
        remainder = count % k
        
        curr = head
        ans = []
        
        
        while k:
            if curr:
               
                take = 0
                if remainder:
                    take = 1
                    remainder -= 1
                     
                temp = curr
                prev = curr
                size = partSize + take
                
                while temp and size > 0:
                    prev = temp
                    temp = temp.next
                    size -= 1
                   
                prev.next = None
                ans.append(curr)
                curr = temp
                
            else:
                ans.append(None)
                
            k -= 1
        
        return ans
                
                
                
                
            
            
            
        
            
        