# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode(next = head)
        head = temp
        self.border = head.next
        
        while self.border and self.border.next :
            
            temp = self.border.next
            self.border.next = self.border.next.next
            self.insert(head, temp)
        
        return head.next
        
        
    def insert(self, head, node):
        
        prev = head
        curr = head.next
        
        while curr and curr.val <= node.val and prev != self.border :
            
            curr = curr.next
            prev = prev.next
         
        node.next = curr
        prev.next = node
        
        if prev == self.border:
            self.border = node
        
        elif not curr:
            self.border = curr

        
        