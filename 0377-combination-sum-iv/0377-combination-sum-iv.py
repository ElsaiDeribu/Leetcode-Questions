class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(idx, target):
            
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            
            count = 0
            
            for i in range(len(nums)):
                
                count +=  dp(i, target - nums[i])
                
            return count
        
        
        return dp(0, target)