# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(post, pre):
            
            if not pre:
                return
            
            if len(pre) == 1:
                return TreeNode(post.pop())
            
            node = TreeNode(post.pop())
            preRightStartIndex = pre.index(post[-1])
            
            node.right = dfs(post, pre[preRightStartIndex:])
            node.left = dfs(post, pre[1 : preRightStartIndex])
            
            return node
            
            
        return dfs(postorder, preorder)
            
        
        
