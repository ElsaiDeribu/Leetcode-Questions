class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        subarrSum = 0
        minLength = 10 ** 6
        
        while r < len(nums):
            subarrSum += nums[r]
            while subarrSum >= target:
                minLength = min(minLength, r - l + 1)
                subarrSum -= nums[l]
                l += 1
                
            r += 1
        
        return 0 if minLength == 10**6 else minLength