# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0      
        def dfs(sum, node, target):
            if node:
                sum += node.val
                print(node.val, sum, target)      
                if sum == target and node.left == None and node.right == None:
                    return True
                return dfs(sum, node.left, target) or dfs(sum, node.right, target)
                
                
        ans = dfs(sum, root, targetSum) 
        print(ans)
        
        return False if not ans else ans
                    
        
       