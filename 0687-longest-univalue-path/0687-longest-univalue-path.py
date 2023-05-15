# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        longest = 0
        
        def dfs(node):
            
            nonlocal longest 
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            if node.left and node.left.val == node.val: left += 1
            else: left = 0
                
            if node.right and node.right.val == node.val: right += 1
            else: right = 0  
            
            longest = max(longest, left + right )
            
            return max(left, right)
            
            
        dfs(root)    
        
        return longest 
                
            