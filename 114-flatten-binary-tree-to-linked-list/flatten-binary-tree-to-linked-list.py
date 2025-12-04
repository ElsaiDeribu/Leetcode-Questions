# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        
        def dfs(node):
            if not node: return

            right = node.right
            node.right = node.left
            
            curr = node.right

            while curr and curr.right:
                curr = curr.right

            if curr:
                curr.right = right
            else:
                node.right = right

            node.left = None

            dfs(node.left)
            dfs(node.right)

            return node


        dfs(root)
