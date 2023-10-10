# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def dfs(total, dic, node):
            
            if not node:
                return 0
            
            total += node.val
            count = dic[total - targetSum]
            dic[total] += 1
            left = dfs(total, dic, node.left)
            right = dfs(total, dic, node.right )
            dic[total] -= 1
            
            return left + right + count
            
        pref = defaultdict(int)
        pref[0] = 1
            
        return dfs(0, pref , root)
    
    
    
    