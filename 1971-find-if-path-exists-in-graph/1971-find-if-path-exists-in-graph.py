

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        parent = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}
    
        def find(x): 
            
            nonlocal parent
            if parent[x] == x:
                return x
             
            parent[x] = find(parent[x])
            
            return parent[x] 
             
            
        def union(x, y):
            
            nonlocal parent
            
            repY = find(y)
            repX = find(x)
            
            if repY == repX:
                return 
                
            if size[repY] < size[repX]:

                parent[repY] = repX 
                size[repX] += size[repY]
                
            else:
                
                parent[repX] = repY 
                size[repY] += size[repX]


            
        for n1, n2 in edges:
        
            union(n1, n2)
            
            
        return find(source) == find(destination)