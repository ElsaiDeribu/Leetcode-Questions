class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        self.minUnf = float("inf")
        
        
        def recur(start, children):
            
            if start == len(cookies):
                
                localMax = max(children)
                self.minUnf = min(localMax, self.minUnf)
                return 
                
            for i in range(k):
                temp = children[:]
                temp[i] += cookies[start]
                if temp[i] < self.minUnf:
                    recur(start + 1, temp)
                
                
        children = [0] * k
        
        recur(0, children)
                
        return self.minUnf
                
                
            
        
        