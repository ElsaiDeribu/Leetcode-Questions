class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        
        
        for rel in relations:
            pre, cour = rel
            indegree[cour - 1] += 1
            adjList[pre - 1].append(cour - 1)
                
        deq = deque([])
        totalTime = [0] * n

        for node in range(n):
            if indegree[node] == 0:
                deq.append(node)
                totalTime[node] = time[node]
           
        
        while deq:
            
            for _ in range(len(deq)):
                node = deq.popleft()
                
                for neighbour in adjList[node]:
                    totalTime[neighbour] = max(totalTime[node] + time[neighbour], totalTime[neighbour])

                    indegree[neighbour] -= 1
                    
                    if indegree[neighbour] == 0:
                        deq.append(neighbour)
                        
            
        return max(totalTime)
            
