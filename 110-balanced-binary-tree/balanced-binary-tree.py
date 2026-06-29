# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node: return 0, True

            left_d, l_val = dfs(node.left)
            right_d, r_val = dfs(node.right)

            if abs(left_d - right_d) > 1:
                return 0, False

            return max(left_d, right_d) + 1, l_val and r_val


        return dfs(root)[1]

