class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        scores = defaultdict(int)
        
        ans = 0
        maximum = float("-inf")
        
        for i in range(len(edges)):
            scores[edges[i]] += i
       
        for item in scores:
            
            if scores[item] > maximum:
                maximum = scores[item]
                ans = item
                
            elif scores[item] ==  maximum:
                if item < ans:
                    ans = item

                
                
        
        return ans    
        
        