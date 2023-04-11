class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        count = 0
        
        def dfs(j):
            
            for i in range(len(isConnected[j])):
                if  i != j and isConnected[j][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
            
        for i in range(len(isConnected)):
            if i not in visited:
                for j in range(len(isConnected[0])):
                    if i != j and isConnected[i][j] == 1 and j not in visited:
                        visited.add(j)
                        dfs(j)
                count += 1
                    
        return count