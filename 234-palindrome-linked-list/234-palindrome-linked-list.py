# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linkedList = []
        
        linkedList.append(head.val)
        
        while head.next:
            head = head.next
            linkedList.append(head.val)
            
        reversedLinkedList = linkedList[::-1]  
        
        for i in range(len(linkedList)):
            if linkedList[i] != reversedLinkedList[i]:
                return False
                
        return True
        
        print(reversedfinalhead)
        print(normalhead)
            
            
        return True
    
            
        
        