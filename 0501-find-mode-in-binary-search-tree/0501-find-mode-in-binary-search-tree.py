# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = defaultdict(int)
        
        def dfs(node):
            if not node: return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
            
            
        dfs(root)
        ans = []
        
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
       
        
        start = True
        
        for item in count:
             
            if start: 
                ans.append(item) 
                start = False
                
            elif count[item] == count[ans[0]]:
                ans.append(item)
                  
                
        return ans
            
        
                
                
            