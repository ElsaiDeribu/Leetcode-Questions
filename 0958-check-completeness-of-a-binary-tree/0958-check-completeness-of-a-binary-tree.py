# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        null_seen = False
        deq = Deque([root])
        
        
        def printLevel():
            temp = []
            
            for i in deq:
                if i == "null":
                    temp.append(i)
                else:
                    temp.append(i.val)
        
            print(temp)
            
            
        while deq:
            printLevel()
            
            for _ in range(len(deq)):
                curr_node = deq.popleft()
                
                if null_seen and curr_node != "null":
                    return False
                
                if curr_node == "null":
                    null_seen = True
                    
                else:    
                    deq.append(curr_node.left) if curr_node.left else deq.append("null")
                    deq.append(curr_node.right) if curr_node.right else deq.append("null")
                    
                    
        return True