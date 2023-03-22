# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        pref = defaultdict(int)
        pref[0] = 1
        self.count = 0
        
        def dfs(runningSum, node):
            
            if not node:
                return
            
            runningSum += node.val
            complement = runningSum - targetSum 
            self.count += pref[complement]
            
            pref[runningSum] += 1
            
            dfs(runningSum, node.left)
            dfs(runningSum, node.right)
            
            pref[runningSum] -= 1
            
        dfs(0, root) 
        
        return self.count