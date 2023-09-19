class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                
                nums[nums[i] - 1], nums[i] =  nums[i], nums[nums[i] - 1]
                
