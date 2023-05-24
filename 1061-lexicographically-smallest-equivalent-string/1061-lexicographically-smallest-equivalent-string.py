class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent  = {chr(i):chr(i) for i in range(97, 123)}
        
        
        def find(x):
            nonlocal parent
            
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
                
            return x
        
        
        def union(x, y):
            nonlocal parent
            
            repX = find(x)
            repY = find(y)
            
            if repX == repY:
                return
            
            if repX < repY:
                
                parent[repY] = repX
                
            else:
                parent[repX] = repY
                
                
        for i in range(len(s1)):
            union(s1[i], s2[i]) 
            
        baseStr = list(baseStr)
        
        for i in range(len(baseStr)):
            baseStr[i] = find(baseStr[i]) 
            
            
        return  ''.join(baseStr)
                
                
        
            