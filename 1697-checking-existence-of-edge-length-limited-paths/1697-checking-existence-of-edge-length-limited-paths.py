class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        ans = [False] * len(queries) 
        parent = {i:i for i in range(n)}
        
        edgeList.sort(key = lambda x: x[2])
        
        for i in range(len(queries)):
            queries[i].append(i)
            
        queries.sort(key = lambda x: x[2])
        
        
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
            
            parent[repX] = repY
            
            
        j = 0
        for i in range(len(queries)):
            while j < len(edgeList) and edgeList[j][2] < queries[i][2]:
                n1 = edgeList[j][0]
                n2 = edgeList[j][1]
                union(n1, n2)
                j += 1
                
            n1 = queries[i][0]
            n2 = queries[i][1]
            
            if find(n1) == find(n2):
                ans[queries[i][3]] = True

        return ans
            
            
            
            
            
            
            
            
            
            
    