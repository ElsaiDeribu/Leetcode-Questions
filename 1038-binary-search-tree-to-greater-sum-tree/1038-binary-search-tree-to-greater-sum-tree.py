# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        

        def dfs(curr_node, accumulated_val):
            if not curr_node:
                return accumulated_val
            
            accumulated_right_val = dfs(curr_node.right, accumulated_val)
            curr_node.val += accumulated_right_val
            accumulated_left_val = dfs(curr_node.left, curr_node.val)
        
          
            return accumulated_left_val  
        
        dfs(root, 0)
        
        return root