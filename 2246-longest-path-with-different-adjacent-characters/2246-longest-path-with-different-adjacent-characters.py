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
            
            
#             if len(adjList[node]) == 2:
#                 left = dfs(adjList[node][0])
#                 right = dfs(adjList[node][1])
                
#                 poss1 = left[1] + right[1] + 1 if left[0] != right[0] != s[node] else 1
                
#                 poss2 = left[1] + 1 if left[0] != s[node] else 1
#                 poss3 = right[1] + 1 if right[0] != s[node] else 1
                
#                 ans = max(ans, poss1, poss2, poss3)
                
#                 return [s[node], max(poss2, poss3)]   
                
                
#             elif len(adjList[node]) == 1:
                
#                 res = dfs(adjList[node][0])
#                 poss = res[1] + 1 if res[0] != s[node] else 1
                
#                 ans = max(ans, poss)
                
#                 return [s[node], poss]
                
                
        dfs(0)
        
        return ans
                
                