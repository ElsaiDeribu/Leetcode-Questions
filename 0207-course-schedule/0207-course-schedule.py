class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = [[] for _ in range(numCourses)]
        preCount = defaultdict(int)
        deq = deque([])
        order = []
        
        for pair in prerequisites:
            adjList[pair[1]].append(pair[0])
            preCount[pair[0]] += 1
            
          
        
        for key in range(numCourses):
            if preCount[key] == 0:
                deq.append(key)
        
                
        while deq:
            
            for _ in range(len(deq)):
                pre = deq.popleft()
                
                for child in adjList[pre]:
                    preCount[child] -= 1
                    
                    if preCount[child] == 0:
                        deq.append(child)
                        
                order.append(pre)  
                
            
        return len(order) == numCourses
                    
                    
        