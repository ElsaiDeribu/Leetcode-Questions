# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ans =[]
        
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        newNode = head = TreeNode(ans[0])
        
        for i in range(1, len(ans)):
            head.right = TreeNode(ans[i])
            head = head.right
            
            
        return newNode
        