# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        tree1 = []
        tree2 = []
        
        def dfs1(node):
            if not node:
                return 
            
            dfs1(node.left)
            tree1.append(node.val)
            dfs1(node.right)
            
        def dfs2(node):
            if not node:
                return 
            
            dfs2(node.left)
            tree2.append(node.val)
            dfs2(node.right)
        
        
        dfs1(root1)
        dfs2(root2)
        
        i = 0
        j = 0
        ans = []
        
        while len(ans) < len(tree1) + len(tree2):
            while (i < len(tree1) and j >= len(tree2)) or (i < len(tree1) and tree1[i] <= tree2[j]):
                ans.append(tree1[i])
                i += 1
            
            while (j < len(tree2) and i >= len(tree1)) or (j < len(tree2) and tree2[j] < tree1[i]):
                ans.append(tree2[j])
                j += 1
            
            
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        