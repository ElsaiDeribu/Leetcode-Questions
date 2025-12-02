# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def dfs(pre_start, pre_end, in_start, in_end):

            if pre_start > pre_end or in_start > in_end:
                return

            node_val = preorder[pre_start]
            node = TreeNode(node_val)

            i = in_start
            while inorder[i] != node_val:
                i += 1

            left_len = i - in_start

            node.left = dfs(
                pre_start + 1,
                pre_start + left_len,
                in_start, 
                i - 1
                 )

            node.right = dfs(
                pre_start + left_len + 1,
                pre_end,
                i + 1,
                in_end
                )

            return node


        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)



        
