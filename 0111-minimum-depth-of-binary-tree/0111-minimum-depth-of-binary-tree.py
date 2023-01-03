# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def findMinDepth(node):
            
            if not node:
                return 0
            
            leftDepth = findMinDepth(node.left)
            rightDepth = findMinDepth(node.right)
            
            return max(leftDepth, rightDepth) + 1  if leftDepth == 0 or rightDepth == 0 else min(leftDepth, rightDepth) + 1
        
        
        return findMinDepth(root)