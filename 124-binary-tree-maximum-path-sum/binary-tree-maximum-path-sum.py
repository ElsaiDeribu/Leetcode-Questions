class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node: return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            through = left + node.val + right

            ans = max(ans, through)

            return max(left, right) + node.val


        dfs(root)

        return ans