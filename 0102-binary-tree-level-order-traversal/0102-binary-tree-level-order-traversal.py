# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        deq = Deque([root])
        
        def addLayer():
            temp = []
            for i in range(len(deq)):
                if deq[i]:
                    temp.append(deq[i].val)
            ans.append(temp)
                
                
        while deq:
            addLayer()
            for i in range(len(deq)):
                curr = deq.popleft()
                
                if curr:
                    deq.append(curr.left)
                    deq.append(curr.right)
        
        ans.pop()
        return ans