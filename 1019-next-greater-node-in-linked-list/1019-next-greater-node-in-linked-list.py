# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        ans = []
        curr = head
        
        while curr:
            ans.append(curr.val)
            curr = curr.next
            
        stack = []
        
        for i in range(len(ans)):
            
            while stack and ans[stack[-1]] < ans[i]:
                temp = stack.pop()
                ans[temp] = ans[i] 
                
            stack.append(i)
            
        for item in stack:
            ans[item] = 0
            
        
        return ans