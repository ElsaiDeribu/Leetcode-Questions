class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                
        j = i = 0
        
        while j < len(nums):
            if nums[j] == 0:
                j += 1
                
            elif j < len(nums):   
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1

                    
        return nums
