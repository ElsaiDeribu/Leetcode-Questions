# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        
        right = mid.next
        mid.next = None
        left = head
        
        mergedLeft = self.sortList(left)
        mergedRight = self.sortList(right)
        
        return self.merge(mergedLeft, mergedRight)
        
        
      
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, list1, list2):
        
        merged = ListNode()
        ptr = merged
        
        while list1 and list2:
            
            if list1.val > list2.val:
                ptr.next = ListNode(list2.val)
                ptr = ptr.next
                list2 = list2.next
            
            else:
                ptr.next = ListNode(list1.val)
                ptr = ptr.next
                list1 = list1.next
                
        if list1:
            ptr.next = list1
            
        if list2:
            ptr.next = list2
            
        return merged.next
                
                
                
                
            
            
            
            
        