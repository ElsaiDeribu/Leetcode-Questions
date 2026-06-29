# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node: return 0

            left_d = dfs(node.left)
            if left_d == -1: return -1

            right_d = dfs(node.right)
            if right_d == -1: return -1

            if abs(left_d - right_d) > 1: return -1

            return max(left_d, right_d) + 1


        return dfs(root) != -1

