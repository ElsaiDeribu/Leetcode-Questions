class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def steal(curr):
            
            if curr >= len(nums):
                return 0
            
            largest = max(steal(curr + 2), steal(curr + 3))
            
            return nums[curr] + largest
        
        
        return max(steal(0), steal(1))
                