class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        
        adjList = defaultdict(list)
        ans = 1
        
        for i in range(len(parent)):
            adjList[parent[i]].append(i)
            
            
        def dfs(node):
            nonlocal ans
            if node not in adjList:
                return [s[node], 1]   
            
            last = 1
            for child in adjList[node]:
                res = dfs(child)
                poss = res[1] + 1 if res[0] != s[node] else 1
                
                ans = max(ans, (last + poss - 1) )
                
                last = max(last, poss)

            return [s[node], last]  
                
                
        dfs(0)
        
        return ans
                
                