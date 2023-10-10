# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def dfs(node1, node2):
            if not node1 or not node2:
                if not node1 and not node2:
                    return True
                
                return False
            
            if node1.val != node2.val:
                return False


            #flip

            res1 = dfs(node1.left, node2.right)
            res2 = dfs(node1.right, node2.left)
            
            #don't flip
            
            res3 = dfs(node1.left, node2.left)
            res4 = dfs(node1.right, node2.right)
            
            return (res2 and res1) or (res3 and res4)
            
            
        return dfs(root1, root2)

            