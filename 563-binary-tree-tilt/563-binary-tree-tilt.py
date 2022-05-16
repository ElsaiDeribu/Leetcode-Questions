# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.sumOfTilts = 0
            
        
        def recursion(n):   
            if n.left or n.right:          
                left = recursion(n.left) if n.left else 0
                right = recursion(n.right) if n.right else 0
                self.sumOfTilts += abs(right - left)
                return ( right  + left + n.val )
            else:
                 return n.val
            
        recursion(root)
        return self.sumOfTilts
        
        
        