class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        prev = res = 0
        
        for curr in values:
            
            res = max(res, curr + prev )
            prev = max(prev, curr) - 1
            
            
        return res