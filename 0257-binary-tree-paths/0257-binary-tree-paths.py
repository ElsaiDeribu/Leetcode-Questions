# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        path = []
        
        def preOrder(node):
            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append("->".join(path))
                return 
                
            if node.left:
                preOrder(node.left) 
                if path:
                    path.pop()
            if node.right:
                preOrder(node.right)
                if path:
                    path.pop()

        preOrder(root)    
        
        return ans