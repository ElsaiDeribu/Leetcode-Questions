# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def construct(pre):
            if not pre:
                return None
            
            if len(pre) == 1:
                return TreeNode(pre[0])
            
            
            node = TreeNode(pre[0])
            
            splitIndex = len(pre)
            for i in range(1, len(pre)):
                if pre[i] > pre[0]:
                    splitIndex = i
                    
                    break
                    
            node.left = construct(pre[1 :splitIndex])
            node.right = construct(pre[splitIndex :])
            
            
            return node
            
        return construct(preorder)