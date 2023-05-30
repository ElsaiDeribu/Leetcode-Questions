class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}
        ans = [True] * len(requests)
        
        
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
            
            if size[repX] >= size[repY]:
                parent[repY] = repX
                size[repX] += size[repY]
                
            else:
                parent[repX] = repY
                size[repY] += size[repX]
                
            
        
        for i in range(len(requests)):
            
            n1 = requests[i][0]
            p1 = find(n1)
            n2 = requests[i][1]
            p2 = find(n2)
            
            conn = {p1, p2}
            
            
            for r1, r2 in restrictions:
                if {find(r1), find(r2)} == conn :
                    ans[i] = False
                    break
            else:
                union(n1, n2)
                

        return ans
        
        