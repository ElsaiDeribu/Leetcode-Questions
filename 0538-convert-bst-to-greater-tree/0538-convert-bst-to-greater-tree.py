# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(curr_node, current_cummulative_val):
            if not curr_node:
                return current_cummulative_val
            
            
            cummulative_right_val = dfs(curr_node.right, current_cummulative_val)
            curr_node.val += cummulative_right_val
            cummulative_left_val = dfs(curr_node.left, curr_node.val )
        
            return cummulative_left_val
        
        dfs(root, 0)
        
        return root