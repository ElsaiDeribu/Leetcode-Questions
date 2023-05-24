class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent = {i:i for i in range(1, n + 1)}
        repMin = defaultdict(lambda:10**5)
        
        def find(x):
            nonlocal parent
            
            while parent[x] != x: 
                parent[x] = parent[parent[x]]
                x = parent[x]
                
            return x
            
        
        
        def union(x, y, w):
            nonlocal parent
            
            repX = find(x)
            repY = find(y)
            repMin[repY] = min(repMin[repY], repMin[repX], w)

            if repX == repY:
                return 
            
            
            parent[repX] = repY 
            
            
        for c1, c2, w in roads:
            
            union(c1, c2, w)
            
            
        return repMin[find(1)]
            
            
            