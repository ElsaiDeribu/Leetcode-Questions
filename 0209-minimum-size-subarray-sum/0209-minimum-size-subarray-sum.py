class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = r = 0
        minimalLen = 10**6
        subArrSum = nums[0]
        
        while r < len(nums):
            while subArrSum >= target:
                minimalLen = min(minimalLen, r - l + 1)
                subArrSum -= nums[l]
                l += 1
                
            r += 1
            if r < len(nums):
                subArrSum += nums[r]
            
        return 0 if minimalLen == 10**6 else minimalLen
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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