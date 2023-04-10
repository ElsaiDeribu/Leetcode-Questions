class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        recStack = []
        paths = []
        
        def dfs(index):
             
            recStack.append(index)
            
            if index == len(graph) - 1:
                paths.append(recStack[:])
                return
            

            for nodeIndex in graph[index]:
                dfs(nodeIndex)
                recStack.pop()
        
        dfs(0)
        
        return paths
            