# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        prev = []
        total = 0
        
        def dfs(node):
            nonlocal total
            
            if not node:
                return
            
            if len(prev) >= 2 and prev[-2] % 2 == 0:
                total += node.val
                
            prev.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
            prev.pop()
            
        dfs(root)
        
        
        return total
                
        
        