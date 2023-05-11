class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        conn = defaultdict(int)
        adjList = [[] for _ in range(n)]
        dq = deque([])
        
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            
            conn[n1] += 1
            conn[n2] += 1
            
            
        for c in conn:
            if conn[c] == 1:
                dq.append(c)
                
                
        lastLevel = [0]
        
        while dq:
            lastLevel = dq.copy()
            
            for _ in range(len(dq)):
                node = dq.popleft()
                
                for child in adjList[node]:
                
                    conn[child] -= 1
                    if conn[child] == 1:
                        dq.append(child)


        return list(lastLevel)
            
            
        
        