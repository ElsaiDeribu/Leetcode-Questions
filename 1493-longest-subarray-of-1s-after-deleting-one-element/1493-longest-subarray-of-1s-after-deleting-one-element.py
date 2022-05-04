class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right = 0
        left = 0
        largest = 0
        k = 1
        while right < len(nums):
            
            if nums[right] == 0:
                k -= 1
                
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            largest = max(largest, right - left  )
            
            right += 1
            
        return largest
            
                