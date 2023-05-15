class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        longest = -1
        color = defaultdict(int)
        label = defaultdict(int)
        
        def dfs(node, count):
            
            
            nonlocal longest
            if color[node] == 2 :
                return
            
            if color[node] == 1:
                longest = max(longest, count - label[node])
                return 
            
            
            color[node] = 1
            label[node] = count
            
            if edges[node] != -1:
                dfs(edges[node], count + 1)
            
            color[node] = 2
            
            
        for i in range(len(edges)):
            if edges[i] != -1:
                dfs(i, 0)
            
            
        return longest
            
             
                    
                
                