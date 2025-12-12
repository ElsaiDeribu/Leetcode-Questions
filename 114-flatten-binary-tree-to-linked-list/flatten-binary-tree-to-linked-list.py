class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def dfs(node):
            if not node:
                return

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if left_tail:
                temp = node.right
                node.right = node.left
                node.left = None
                left_tail.right = temp

            return right_tail or left_tail or node

        return dfs(root)
            

