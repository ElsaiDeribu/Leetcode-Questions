# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
                
        
        def dfs(n):
            if n:
                if n.val == target.val:
                    return n
                else:
                    return dfs(n.left) or dfs(n.right) 
            else:
                return

                        
                            
                
        return dfs(cloned) 
            
            
            
        