class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        
        for i in range(len(nums)):
            
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]