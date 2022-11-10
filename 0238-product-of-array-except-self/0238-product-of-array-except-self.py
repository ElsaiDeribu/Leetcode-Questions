class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefProd = [0] * len(nums)
        suffProd = [0] * len(nums)
        prefProd[0] = nums[0]
        suffProd[-1] = nums[-1]
        
        for i in range(1,len(nums)):
            prefProd[i] = prefProd[i - 1] * nums[i] 
            
        for i in reversed(range(len(nums) - 1)):
            suffProd[i] = suffProd[i + 1] * nums[i]
            
       
        ans = [0] * len(nums)
        ans[0] = suffProd[1]
        ans[-1] = prefProd[-2]
        
        for i in range(1, len(nums) - 1):
            ans[i] = prefProd[i - 1] * suffProd[i + 1]
            
        return ans
        
        
        
        
        