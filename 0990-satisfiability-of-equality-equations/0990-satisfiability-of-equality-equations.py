class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = {chr(i): chr(i) for i in range(97, 123)}
        size = {chr(i):1 for i in range(97, 123)}
  
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
            
            if size[repX] > size[repY]:
                parent[repY] = repX
                size[repX] += size[repY]
                
            else:
                parent[repX] = repY
                size[repY] += size[repX]
                
                
        for eq in equations:
            sign = eq[1:3]
            
            if sign == '==':
                union(eq[0], eq[-1])
                
                
        for eq in equations:
            sign = eq[1:3]
            
            if sign == "!=" and find(eq[0]) == find(eq[-1]) :
                return False
            
        return True

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            