# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
            if k == 0:
                return [target.val]
            
            adjList = defaultdict(list)
            deq = deque([])
            
            def dfs(node):
                
                if node.val == target.val:
                    deq.append(node.val)
                    
                if node.right:
                    adjList[node.val].append(node.right.val)
                    adjList[node.right.val].append(node.val)
                    dfs(node.right)
                
                if node.left:
                    adjList[node.val].append(node.left.val)
                    adjList[node.left.val].append(node.val)
                    dfs(node.left)
                    
                    
            dfs(root)
            
            visited = set()
            visited.add(target.val)
            dis = 0
            
            while deq and dis != k:
                
                dis += 1
                for _ in range(len(deq)):
                    node = deq.popleft()
                    
                    for child in adjList[node]:
                        if child not in visited:
                            visited.add(child)
                            deq.append(child)
            
                
            return list(deq)