# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.currCount = 0
        
        def inOrder(node):
            
            if not node:
                return None
            
            
            result1 =  inOrder(node.left)
            self.currCount += 1
                
            if self.currCount == k:
                return node.val
            
            result2 = inOrder(node.right)
             
            
            return result1 if result1 != None  else result2
        
    
        return inOrder(root)