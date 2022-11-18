class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = 10**6
        subSum = 0
        l = 0
        for r in range(len(nums)):
            subSum += nums[r]
            while subSum - nums[l] >= target:
                subSum -= nums[l]
                l += 1
                
            if subSum >= target:
                minLength = min(minLength, r - l + 1)
        
        
        return minLength if minLength != 10**6 else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l = 0
#         r = 0
#         subarrSum = 0
#         minLength = 10 ** 6
        
#         while r < len(nums):
#             subarrSum += nums[r]
#             while subarrSum >= target:
#                 minLength = min(minLength, r - l + 1)
#                 subarrSum -= nums[l]
#                 l += 1
                
#             r += 1
        
#         return 0 if minLength == 10**6 else minLength