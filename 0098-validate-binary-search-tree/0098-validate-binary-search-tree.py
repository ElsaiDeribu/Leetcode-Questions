# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def dfs(curr_node, minimum, maximum):
            
            if not curr_node:
                return 
            
            left_val = dfs(curr_node.left, minimum, curr_node.val)
            
            right_val = dfs(curr_node.right, curr_node.val, maximum)
            
            
            if curr_node.val <= minimum or curr_node.val >= maximum:
                self.ans = False
                
            
            return curr_node.val
            
            
        dfs(root, float("-inf"), float("inf"))  
        
        return self.ans
        