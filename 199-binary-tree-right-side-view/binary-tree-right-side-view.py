# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def dfs(node, h):
            if not node: return 

            h += 1
            if len(ans) < h:
                ans.append(node.val)

            ans[h - 1] = node.val
            
            dfs(node.left, h)
            dfs(node.right, h)

        dfs(root, 0)

        return ans
        