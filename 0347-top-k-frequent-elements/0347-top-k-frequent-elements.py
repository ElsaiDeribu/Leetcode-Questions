class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        return list(dict(sorted(Counter(nums).items(), key = lambda x: x[1], reverse = True)).keys())[:k]
        
    
     
        
        