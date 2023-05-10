class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        ans = []
        colors = [0] * len(graph) 
        
        def dfs(node):
            
            if colors[node] == 1:
                return False
            
            if colors[node] == 2:
                return True
            
            
            colors[node] = 1
            
            for child in graph[node]:
                if not dfs(child):
                    return False
                
            colors[node] = 2
            
            return True
                    

        
        for i in range(len(graph)):
            
            if dfs(i):
                ans.append(i)
                
        return ans