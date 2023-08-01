class Solution:
    def rob(self, nums: List[int]) -> int:
        
        past, present = 0, 0
        ans = 0
        
        for i in range(len(nums)):
            
            ans = max(past + nums[i], present)
            
            past = present
            present = ans
                
        
        return ans
            
            
            
        
   