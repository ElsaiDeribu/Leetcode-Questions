class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def dp(remain):
            
            if remain < 0:
                return 0
            
            if remain == 0:
                return 1
            
            res = 0
            for i in range(len(nums)):
                res += dp(remain - nums[i])
                
            return res 
        
        ans = dp(target) 
        
        return ans