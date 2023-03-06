# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        count1 = 1
        curr = l1
        
        while curr:
            count1 += 1
            curr = curr.next
            
        curr = l2
        count2 = 1
        while curr:
            count2 += 1
            curr = curr.next
            
        lHead = l1
        sHead = l2
        
        if count1 < count2:
            lHead = l2
            sHead = l1
            
            
        remain = 0
        
        currL = lHead
        currS = sHead
        
        while currS:
            
            result = str(currL.val + currS.val + remain) 
            if len(result) > 1:
                remain = int(result[0])
                result = int(result[1])
            else:
                remain = 0
                
            currL.val = result
            
            currS = currS.next
            if currS:
                currL = currL.next
            
        while remain != 0:
            
            if currL.next:
                    
                currL = currL.next
                result = str(currL.val + remain) 
                
                if len(result) > 1:
                        remain = int(result[0])
                        result = int(result[1])
                else:
                    remain = 0
                    
                currL.val = result
                
            else:
                currL.next = ListNode(remain)
                remain = 0

        return lHead
                

                
            
            
            
            
            
            
            
        
            
        
        
        