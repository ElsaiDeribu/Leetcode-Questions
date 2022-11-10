class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        suffSum = [0] * len(nums)
        prefSum = [0] * len(nums)
        suffSum[-1] = nums[-1]
        prefSum[0] = nums[0]
        
        if len(nums) == 1:
            return 0
        
        for i in range(1,len(nums)):
            prefSum[i] = prefSum[i - 1] + nums[i]
        
        for i in reversed(range(len(nums) - 1)):
            suffSum[i]  = suffSum[i + 1] + nums[i]
        
        
        if suffSum[1] == 0:
            return 0
            
        for i in range(1, len(nums) - 1):
            if prefSum[i - 1]  == suffSum[i + 1]:
                return i

        if prefSum[-2] == 0:
            return len(nums) - 1
        
        
        return -1
                