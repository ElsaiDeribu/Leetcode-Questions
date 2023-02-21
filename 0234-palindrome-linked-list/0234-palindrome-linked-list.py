# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        linkedList = []
        
        ptr = head
        
        while ptr:
            linkedList.append(ptr)
            
            ptr = ptr.next
            
        right = len(linkedList) - 1
        left = 0
        
        
        while left < right:
            if linkedList[left].val != linkedList[right].val:
                return False
            
            left += 1
            right -= 1
            
        return True
            
            