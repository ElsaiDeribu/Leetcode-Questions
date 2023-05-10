class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adjList = [[] for _ in range(n)]
        deq = deque([])
        indegree = defaultdict(int)
        ancestors = [set() for _ in range(n)]
        
        
        for edge in edges:
            frm = edge[0]
            to = edge[1]
            
            adjList[frm].append(to)
            indegree[to] += 1
         
        
        for node in range(n):
            if indegree[node] == 0:
                deq.append(node)
                
            
        while deq:
            
            for _ in range(len(deq)):
                
                node = deq.popleft()
                
                for child in adjList[node]:
                    indegree[child] -= 1
                    ancestors[child] = ancestors[child].union(ancestors[node])
                    
                    ancestors[child].add(node)
                    if indegree[child] == 0:
                        deq.append(child)
           
        for i in range(len(ancestors)):
            ancestors[i] = list(sorted(ancestors[i]))
                
        return ancestors