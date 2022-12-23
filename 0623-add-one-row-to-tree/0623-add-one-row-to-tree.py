# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
#         handle edge cases
        if depth == 1: 
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        deq = Deque([root])
        curr_level = 1

        
#       Level order traversal to find the level and replace it
        while deq:
            
#       replace the current level
            for i in range(len(deq)):
                curr_node = deq.popleft()
                if curr_level == depth - 1: 
                        temp = curr_node.left
                        curr_node.left = TreeNode(val)
                        curr_node.left.left = temp
                        
                        temp = curr_node.right
                        curr_node.right = TreeNode(val)
                        curr_node.right.right = temp
                  
                else:        
                    deq.append(curr_node.left) if curr_node.left else None 
                    deq.append(curr_node.right) if curr_node.right else None
        
            curr_level += 1
            
        return root