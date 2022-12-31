# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        def construct(post, inord):
            
            if not inord:
                return
            
            if len(inord) == 1:
                
                return TreeNode(post.pop())
            
            
            splitIndex = inord.index(post[-1]) 
            node = TreeNode(post.pop())
             
            
            
            node.right= construct(post, inord[splitIndex + 1 : ] )
            node.left = construct(post,  inord[ :splitIndex] )
            
            return node
        
        return construct(postorder, inorder)