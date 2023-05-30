class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dp(n, curr):
            
            if (n, curr) in memo:
                return memo[(n, curr)]
            
            if n >= len(nums):
                if curr == target:
                    return 1
                return 0
        
            right = dp(n + 1, curr - nums[n])
            left = dp(n + 1, curr + nums[n])
            
            memo[(n,curr)] = left + right
            
            return memo[(n,curr)]
            

        return dp(0, 0)
        
        
                

                
                
            
            
            
            