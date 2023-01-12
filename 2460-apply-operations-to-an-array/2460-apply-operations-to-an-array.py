class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                
                
                
#         left = 0
        
#         for right in range(len(nums)):
#             if nums[right]:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
             
    
    
        j = i = 0
        
        while j < len(nums):
            
            if nums[j]:   
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            
            j += 1 

        
        return nums

                

                    
