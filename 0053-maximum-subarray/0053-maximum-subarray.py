class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sumUpToNow = 0
        minSum = 0
        maxSubArrSum = -10**6
        
        for i in range(len(nums)):
            
            sumUpToNow += nums[i]
            maxSubArrSum = max(maxSubArrSum, sumUpToNow - minSum)
            minSum = min(minSum, sumUpToNow)
            
            
        return maxSubArrSum
            
            