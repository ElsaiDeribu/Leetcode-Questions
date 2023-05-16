class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adjList = [[] for _ in range(n)]
        deq = deque([])
        indegree = defaultdict(int)
        ancestors = [set() for _ in range(n)]
        
        
        for frm, to in edges:
            
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
                    
                    ancestors[child].add(node)
                    ancestors[child].update(ancestors[node])
                    
                    if indegree[child] == 0:
                        deq.append(child)
           
        for i in range(len(ancestors)):
            ancestors[i] = sorted(ancestors[i])
                
        return ancestors