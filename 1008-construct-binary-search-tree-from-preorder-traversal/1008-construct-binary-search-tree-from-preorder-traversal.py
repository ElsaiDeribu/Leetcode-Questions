# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def build(arr):
            
            if len(arr) == 0:
                return
            
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            node = TreeNode(arr[0])
            splitIndex = len(arr)
            
            for i in range(1, len(arr)):
                if arr[i] > arr[0]:
                    splitIndex = i
                    break
                    
            
            node.left = build(arr[1:splitIndex])   
            node.right = build(arr[splitIndex:])
            
            
            return node
        
        return build(preorder)
            
            