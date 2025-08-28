# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def dfs(leaf, node):

            if (not node.left) and (not node.right):
                leaf.append(node.val)
                return

            dfs(leaf, node.left) if node.left else None
            dfs(leaf, node.right) if node.right else None


        leaf1 = []
        leaf2 = []

        dfs(leaf1, root1)
        dfs(leaf2, root2)

        return leaf1 == leaf2