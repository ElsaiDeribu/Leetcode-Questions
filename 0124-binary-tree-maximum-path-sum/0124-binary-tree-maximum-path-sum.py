# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        ans = float("-inf")        
        
        def dfs(node):
            
            nonlocal ans
            
            if (not node.left) and (not node.right):
                ans = max(ans, node.val)
                return node.val
            
            left = node.val
            right = node.val
            if node.left:
                left += dfs(node.left)
            
            if node.right:
                right += dfs(node.right)
                
            ans = max(ans, left, right, node.val, left+right-node.val)
            
            return max(node.val, left, right, 0)
        
        dfs(root)
        

        return ans 
        
        
        