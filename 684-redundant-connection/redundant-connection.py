class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = {i:i for i in range(1, len(edges) + 1)}
        size = {i:1 for i in range(1, len(edges) + 1)}
        
        
        def find(x): 
            
            nonlocal parent
            
            if parent[x] == x: 
                return x
                
            parent[x] = find(parent[x]) # find_parent(parent[x])
            
            return parent[x]
        
        
        def union(x, y):
            
            nonlocal parent
            
            repX = find(x)
            repY = find(y)
            
            if repX == repY:
                return [x, y]
            
            if size[repX] < size[repY]:
                
                parent[repX] = repY
                size[repY] += size[repX]
                
            else:
                parent[repY] = repX
                size[repX] += size[repY]
                
        ans = []       
        for n1, n2 in edges:
            res = union(n1, n2) 
            
            if res:
                ans = res  
        
        return ans
            