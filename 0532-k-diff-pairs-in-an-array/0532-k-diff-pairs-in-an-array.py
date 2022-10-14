class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = Counter(nums)
        kdiff = 0
        
        for i in count.keys():
            
            if k > 0:
                if i + k in count:
                    kdiff += 1
                    
            else:
                if count[i] >= 2:
                    kdiff += 1
        
        
        return kdiff