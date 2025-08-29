class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        ans = 0

        def dfs(n):
            visited.add(n)

            for i in range(len(isConnected)):
                if i not in visited:
                    if isConnected[n][i] == 1:
                        dfs(i)


        for n in range(len(isConnected)):
            if n not in visited:
                ans += 1
                dfs(n)


        return ans