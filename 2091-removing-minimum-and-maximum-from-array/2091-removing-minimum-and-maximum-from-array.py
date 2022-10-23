class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        
        maxIndex = nums.index(max(nums))
        minIndex = nums.index(min((nums)))
        
        l = minIndex
        r = maxIndex
        
        
        if l > r:
            
            l, r = r, l
            
        
        candidate1 = len(nums) - l
        candidate2 = r + 1
        candidate3 = l+1 + len(nums) - r
        
        return min(candidate1, candidate2, candidate3)
        
        
        
        
        
        
        
        
        
        