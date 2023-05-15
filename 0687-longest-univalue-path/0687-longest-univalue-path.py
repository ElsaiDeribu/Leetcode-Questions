# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        longest = 1
        
        if not root:
            return 0
        
        def dfs(node):
            
            nonlocal longest 
            
            if not node.left and not node.right:
                return [node.val, 1]
            
            through = 0
            left, right = ["", 0], ["", 0]
            
            if node.left:
                left = dfs(node.left)
                    
            if node.right: 
                right = dfs(node.right)
                
                
            if left[1] and right[1] and left[0] == right[0] == node.val:
                through = right[1] + left[1] + 1
            
            if left[1] and left[0] == node.val:
                left[1] += 1
                
            if right[1] and right[0] == node.val:
                right[1] += 1
               
            
            # print(longest, left[1], right[1], through)
            longest = max(longest, left[1], right[1], through)
               
            
            if right[0] == node.val and left[0] == node.val:
                
                if right[1] > left[1]:
                    return right
                
                return left
            
            if right[0] == node.val: return right
                
            if left[0] == node.val : return left
            

            return [node.val, 1]  
            

        dfs(root)
        
        return longest - 1
                
            