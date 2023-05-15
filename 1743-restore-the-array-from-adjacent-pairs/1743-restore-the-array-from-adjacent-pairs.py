class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        order = []
        
        for n1, n2 in adjacentPairs:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            
     
        
        def dfs(node, parent):
            nonlocal order
            
            if len(adjList[node]) == 1:
                order.append(node)
                return

            for child in adjList[node]:
                if child != parent:
                    dfs(child, node)

            
            order.append(node)

        
        for node in adjList:
            if len(adjList[node]) == 1:
                child = adjList[node][0]
                dfs(child, node)
                    
                order.append(node)
                
                return order
       
