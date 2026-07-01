# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, r_max):
            if not node: return 0

            temp = 0
            if node.val >= r_max:
                temp = 1
                r_max = node.val

            left = dfs(node.left, r_max)
            right = dfs(node.right, r_max)

            return left + right + temp

        return dfs(root, float("-inf"))