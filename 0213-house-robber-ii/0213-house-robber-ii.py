class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        
        def steal(nums):
            past, present = 0, 0
            ans = 0

            for i in range(len(nums)):

                ans = max(past + nums[i], present)

                past = present
                present = ans
        
            return ans
        
        return max(steal(nums[1:]), steal(nums[:len(nums) - 1]))
          
