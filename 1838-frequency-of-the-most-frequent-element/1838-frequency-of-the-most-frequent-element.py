class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        
        nums = sorted(nums, reverse = True)  
            
        l = r = 0
        subArrSum = 0
        longest = 0
        
        while r < len(nums):
            
            subArrSum += nums[r]
            
            while nums[l] * (r - l + 1) - subArrSum > k:
                subArrSum -= nums[l]
                l += 1
            
            longest = max(longest, r - l + 1)
            
            r += 1
        
        
        return longest