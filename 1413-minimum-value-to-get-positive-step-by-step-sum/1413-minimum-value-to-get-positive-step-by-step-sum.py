class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        for i in range(1, len(nums)):
            
            nums[i] = nums[i - 1] + nums[i]
            
        minimumPSum = min(nums)
        startValue = 1
        
        if minimumPSum <=  0:
            startValue = -1 * (minimumPSum) + 1
       
        return startValue
        