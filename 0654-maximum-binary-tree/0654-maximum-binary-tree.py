# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def buildTree(arr):
            if not arr:
                return
            
            maxValue = max(arr)
            maxIndex = arr.index(maxValue)
            
            root = TreeNode(maxValue)
            
            root.left = buildTree(arr[:maxIndex])
            root.right = buildTree(arr[maxIndex + 1:])
        
            return root
        

        
        return buildTree(nums)