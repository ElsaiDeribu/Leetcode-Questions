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
                return [None, depth]

            left = node.left if node.left else None
            right = node.right if node.right else None

            left_n, dl = dfs(left, depth + 1)
            right_n, dr = dfs(right, depth + 1)

            if dl == dr:
                return [node, dl]

            elif dl > dr:
                return [left_n, dl]

            return [right_n, dr]

        return dfs(root, 0)[0]

            










