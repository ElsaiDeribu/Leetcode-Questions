# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        beginning,fast, slow = head, head, head
        isOdd = 0
        
        if head.next == None:
            return head
        
        while fast.next and  fast.next.next:
            
            fast = fast.next.next
            slow = slow.next
            
        if not fast.next:
            isOdd = 1
            
        current = slow
        prev = current
        current = current.next
        prev.next = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            
        last = prev
        # print(prev)
        # print(beginning.next)
        
        while last.next and beginning :
   
            nodeToInsert = last
            last = last.next
            nodeToInsert.next = beginning.next
            beginning.next = nodeToInsert
            beginning = nodeToInsert.next
       
        
        
        
        # while beginning:
        #     print(beginning)
        #     temp1 = beginning
        #     beginning = beginning.next
        #     if  isOdd and beginning.next == None :
        #         temp1.next = last
        #         break
        #     temp2 = last
        #     last = last.next
        #     temp2.next = beginning
        #     temp1.next = temp2
            
            
    
            
        return head