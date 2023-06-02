class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parent = {}
        size = {}
        
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
            
            if size[repY] < size[repX]:
                parent[repY] = repX
                size[repX] += size[repY]
                
            else:
                parent[repX] = repY
                size[repY] += size[repX]
                
        
        for i in range(len(stones)):
            stones[i] = tuple(stones[i])
            size[stones[i]] = 1
            parent[stones[i]] = stones[i]
        
        row, col = {}, {}
        for i in range(len(stones)):
            if stones[i][0] in row:
                union(row[stones[i][0]], stones[i])
            if stones[i][1] in col:
                union(col[stones[i][1]], stones[i])
            row[stones[i][0]] = stones[i]
            col[stones[i][1]] = stones[i]
#             for j in range(i + 1, len(stones)):
#                 cell1 = stones[i]
#                 cell2 = stones[j]

#                 if cell1[0] == cell2[0] or cell1[1] == cell2[1]:
#                     union(cell1, cell2)
        
        ans = 0
        visited = set()
        
        for i in range(len(stones)):
            pnt = find(stones[i])
            if pnt not in visited:
                ans += size[pnt] - 1
                visited.add(pnt)
                
                
        return ans
            