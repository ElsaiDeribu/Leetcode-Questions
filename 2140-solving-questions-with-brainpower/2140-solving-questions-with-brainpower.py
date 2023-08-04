class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        @cache
        def future(idx):
            
            if idx >= len(questions):
                return 0
            
            take = future(idx + questions[idx][1] + 1) + questions[idx][0] 
            notTake = future(idx + 1)
            
            return max(take, notTake)
        
        
        return future(0)