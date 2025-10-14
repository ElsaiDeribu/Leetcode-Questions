# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []


        def dfs(node, layer):
            if not node:
                return

            if len(ans) - 1 < layer:
                ans.append(node.val)

            else: 
                ans[layer] = node.val

            dfs(node.left, layer + 1)
            dfs(node.right, layer + 1)

        dfs(root, 0)

        return ans