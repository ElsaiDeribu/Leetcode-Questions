# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        def dfs(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return 

            node_val = postorder[post_end]
            node = TreeNode(node_val)

            i = in_start
            while inorder[i] != node_val:
                i += 1

            left_len = i - in_start

            node.left = dfs(
                in_start,
                i - 1,
                post_start,
                post_start + left_len - 1
            )

            node.right = dfs(
                i + 1,
                in_end,
                post_start + left_len,
                post_end - 1
            )



            return node


        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)


        