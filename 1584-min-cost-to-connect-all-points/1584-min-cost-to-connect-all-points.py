class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        connections = []
        parent = {tuple(p):tuple(p) for p in points} 
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                
                a = tuple(points[i])
                ax = a[0]
                ay = a[1]
                
                b = tuple(points[j])
                bx = b[0]
                by = b[1]
                
                distance = abs(ax - bx) + abs(ay - by)
                
                connections.append((distance,a,b))
        
        connections.sort()
        
        
        
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
                return False
            
            parent[repX] = repY
            
            return True
        
        ans = 0
        
        for edge in connections:
            if union(edge[1], edge[2]):
                ans += edge[0]
            
        return ans
            
            
            
        