# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0      
        def dfs(pathSum, node, target):
            if node:
                pathSum += node.val     
                if pathSum == target and node.left == None and node.right == None:
                    return True
                return dfs(pathSum, node.left, target) or dfs(pathSum, node.right, target)
        
        return dfs(pathSum, root, targetSum) 
                    
        
       