# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0      
        def dfs(pathSum, node):
            if node:
                pathSum += node.val     
                if pathSum == targetSum and node.left == None and node.right == None:
                    return True
                return dfs(pathSum, node.left) or dfs(pathSum, node.right)
        
        return dfs(pathSum, root) 
        