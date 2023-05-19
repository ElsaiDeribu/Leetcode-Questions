class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        connections = []
        parent = {i:i for i in range(len(points))} 
        ans = 0
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                
                p1 = points[i]
                x1, y1 = p1[0], p1[1]
                
                p2 = points[j]
                x2, y2 = p2[0], p2[1]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                
                connections.append((distance, i, j))
                
        connections.sort()
        
        def find(x):
            nonlocal parent
            
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        
        def union(x, y):
            nonlocal parent
            
            repX = find(x)
            repY = find((y))
            
            
            if repX == repY:
                return False
            
            parent[repX] = parent[repY]
            
            return True
        
    
        for edge, p1, p2 in connections:
            
            if union(p1, p2):
                ans += edge
                
                
        return ans
            
            
            
            
            
            
            
            