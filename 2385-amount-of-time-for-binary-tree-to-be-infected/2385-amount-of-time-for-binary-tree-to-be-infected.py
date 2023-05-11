# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        adjList = defaultdict(list)
        deq = deque([])
        
        def dfs(node):
            
            if node.val == start:
                deq.append(node.val)
                
            if node.left:
                adjList[node.left.val].append(node.val)
                adjList[node.val].append(node.left.val)
                dfs(node.left)
                
            if node.right:
                adjList[node.right.val].append(node.val)
                adjList[node.val].append(node.right.val)
                dfs(node.right)
                
        dfs(root)
        
        visited = set() 
        visited.add(start)
        time = -1
        
        while deq:
            
            time += 1
            
            for _ in range(len(deq)):
                
                node = deq.popleft()
                
                for child in adjList[node]:
                    if child not in visited:
                        visited.add(child)
                        deq.append(child)
                
                    
        return time
                    
                    
                
                
                
                
                
                
                
                
                
                
                