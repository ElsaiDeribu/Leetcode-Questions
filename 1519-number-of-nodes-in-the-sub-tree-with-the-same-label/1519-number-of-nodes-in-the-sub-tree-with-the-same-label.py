class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        adjList = [[] for _ in range(n)]
        
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            
              
        visited = set()        
        ans = [1] * n
        
        def dfs(node):
            visited.add(node)
            # if not adjList[node]:
            #     temp = [0] * 26
            #     temp[ord(labels[node]) - 97] += 1 
            #     return temp
            
            curr = [0] * 26
    
            for item in adjList[node]:
                if item not in visited:
                    result = dfs(item)
                    for i in range(len(result)):
                        curr[i] += result[i]
           
            ans[node] += curr[ord(labels[node]) - 97]
            curr[ord(labels[node]) - 97] += 1 
            
            return curr
        
        
        dfs(0)
        
        return ans