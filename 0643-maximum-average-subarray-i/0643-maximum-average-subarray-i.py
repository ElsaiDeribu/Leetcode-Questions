class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l = 0
        r = k - 1
        
        subArrSum = sum(nums[l: r + 1])
        subArrAverage = subArrSum / k
        maxAverage = subArrAverage
        
        while r < len(nums):
            
            r += 1
            if r < len(nums):
                subArrSum += nums[r]
                subArrSum -= nums[l]
                l += 1
            
            subArrAverage = subArrSum / k
            
            maxAverage = max(maxAverage, subArrAverage)
        
        return maxAverage   
        
        
        
        