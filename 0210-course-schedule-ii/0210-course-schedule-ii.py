class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = [[] for _ in range(numCourses)]
        inDeg = defaultdict(int)
        deq = deque([])
        order = []
        
        
        for edge in prerequisites:
            frm = edge[1]
            to = edge[0]
            
            adjList[frm].append(to)
            inDeg[to] += 1
            
            
            
        for i in range(numCourses):
            if inDeg[i] == 0:
                deq.append(i)
                
           
        while deq:

            for _ in range(len(deq)):
                node = deq.popleft()
            
                for child in adjList[node]:
                    inDeg[child] -= 1
                    
                    if inDeg[child] == 0:
                        deq.append(child)
                        
                order.append(node)
         
            
        if len(order) == numCourses:
            return order
        
        return []