class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        edgeCnt = defaultdict(int)
        order = []
        
        for n1, n2 in adjacentPairs:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            
            edgeCnt[n1] += 1
            edgeCnt[n2] += 1
            
        
        def dfs(node, parent):
            nonlocal order
            
            if edgeCnt[node] == 1:
                order.append(node)
                return

            for child in adjList[node]:
                if child != parent:
                    dfs(child, node)

            
            order.append(node)

        
        for node in edgeCnt:
            if edgeCnt[node] == 1:
                child = adjList[node][0]
                dfs(child, node)
                    
                order.append(node)
                break
                
        return order
       
