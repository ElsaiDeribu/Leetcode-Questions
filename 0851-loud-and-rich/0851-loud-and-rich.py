class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        adjList = [[] for _ in range(len(quiet))]
        inDeg = defaultdict(int)
        deq = deque()
        ans = [0] * len(quiet)
        
        
        for rich, poor in richer:
            
            adjList[rich].append(poor)
            inDeg[poor] += 1
        
        
        for i in range(len(quiet)):
            if inDeg[i] == 0:
                deq.append(i)
                
            ans[i] = i
            
            
        while deq:
            
            for _ in range(len(deq)):
                node = deq.popleft()
                
                for child in adjList[node]:
                    
                    inDeg[child] -= 1
                    
                    if quiet[ans[node]] <= quiet[ans[child]]:
                        ans[child] = ans[node]
                    
                    if inDeg[child] == 0:
                        deq.append(child)
                        
                    
        return ans