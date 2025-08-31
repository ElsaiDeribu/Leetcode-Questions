# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(node, mx, ans):
            if not node:
                return ans

            res_l = dfs(node.left, max(mx, node.val), ans)
            res_r = dfs(node.right, max(mx, node.val), ans)

            if node.val >= mx:
                ans += 1

            return res_l + res_r + ans


        return dfs(root, float("-inf"), 0)

