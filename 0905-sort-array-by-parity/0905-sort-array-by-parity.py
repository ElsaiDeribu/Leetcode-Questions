class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        
        ans = []
        
        
        for i in range(len(nums)):
            
            if nums[i] % 2 == 0:
                ans.append(nums[i])
        
        for i in range(len(nums)):
            
            if nums[i] % 2 != 0:
                ans.append(nums[i])
                
                
        return ans