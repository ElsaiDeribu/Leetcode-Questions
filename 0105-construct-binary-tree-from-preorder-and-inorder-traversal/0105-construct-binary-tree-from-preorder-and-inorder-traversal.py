# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = preorder[::-1]
        
        
        def construct(preord, inord):
            if not inord:
                return 
            
            if len(inord) == 1:
                return TreeNode(preord.pop())
            
            splitIndex = inord.index(preord[-1])

            node = TreeNode(preord.pop())
            
            node.left = construct(preord, inord[: splitIndex])
            node.right = construct(preord, inord[splitIndex + 1: ])
            
            
            return node
        
        
        return construct(preorder, inorder)