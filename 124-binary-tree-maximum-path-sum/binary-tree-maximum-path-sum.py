# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        def dfs(node):

            if not node:
                return 0,  float("-inf")

            left_down, left_best = dfs(node.left)
            right_down, right_best = dfs(node.right)

            poss1 = left_down + node.val
            poss2 = right_down + node.val
            poss3 = left_down + node.val + right_down
            poss4 = node.val

            return max(poss1, poss2, poss4), max(left_best, right_best, poss1, poss2, poss3, poss4)

        return dfs(root)[1]