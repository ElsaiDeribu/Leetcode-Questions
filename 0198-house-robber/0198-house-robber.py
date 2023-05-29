class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def rob(n):
            
            if n >= len(nums):
                return 0
            
            if n == len(nums) - 1:
                return nums[-1]
            
            curr = nums[n]
            res = 0
            for i in range(n + 2, len(nums)):
                 res = max(res, rob(i))
                    
            return res + curr
                    
                
                
        return max(rob(0), rob(1))