# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        
        def dfs(node):
            if not node:
                return 0, 0, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            resl, suml, cntl = left
            resr, sumr, cntr = right
            
            res = resl + resr
            sumt = suml + sumr + node.val
            cntt = cntl + cntr + 1
            
            mean = sumt // cntt 
            
            if mean == node.val:
                res += 1
                
            return res, sumt, cntt
        
        
        return dfs(root)[0]
                