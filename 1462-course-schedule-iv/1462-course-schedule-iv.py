class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjList = [[] for _ in range(numCourses)]
        inDeg = defaultdict(int)
        deq = deque([])
        ancestors = [set() for _ in range(numCourses)]
        ans = []
        
        for frm, to in prerequisites:
            
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
                    
                    ancestors[child].add(node)
                    ancestors[child].update(ancestors[node])
                    
                    if inDeg[child] == 0:
                        deq.append(child)
                    
        
        for pre, post in queries:
            
            ans.append(pre in ancestors[post])
        
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        