# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            
            if not node:
                return [0,0]  
            
            left = dfs(node.left)
            
            pastL, presentL = left
                        
            right = dfs(node.right)
            
            pastR, presentR = right
            
            past = pastL + pastR
            present = presentL + presentR
            
            temp = max(node.val + past, present)
            
            past = present
            present = temp
            
            return [past, present]
            

        return dfs(root)[1]    
            

        
        
        
        
            