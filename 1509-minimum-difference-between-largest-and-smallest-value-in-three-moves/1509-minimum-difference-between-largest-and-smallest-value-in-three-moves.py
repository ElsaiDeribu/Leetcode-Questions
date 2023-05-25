class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if len(nums) > 4:
            ans = float("inf")
            
            for i in range(4):
                maximum = nums[-(4-i)] 
                minimum  = nums[i]

                ans = min(ans, maximum - minimum)
                
            return ans
        
        return 0
        
        