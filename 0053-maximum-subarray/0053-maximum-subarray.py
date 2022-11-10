class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        prefSum = [0] * len(nums)
        prefSum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefSum[i] = prefSum[i - 1] + nums[i]
        
        
        largestSum = -10**6
        minleftSum = 0
        
        for i in range(len(prefSum)):
            largestSum = max(largestSum, prefSum[i] - minleftSum )
            minleftSum = min(minleftSum, prefSum[i])
            
        return largestSum