# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node, depth):
            if not node:
                return None, depth

            left_n, dl = dfs(node.left, depth + 1)
            right_n, dr = dfs(node.right, depth + 1)

            if dl == dr:
                return node, dl

            elif dl > dr:
                return left_n, dl

            return right_n, dr

        return dfs(root, 0)[0]

            










