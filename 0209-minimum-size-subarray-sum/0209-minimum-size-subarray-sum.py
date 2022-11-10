class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
                
            i = 0
            j = 0
            minLength = 10**9
            windowSum = nums[i]


            while j < len(nums):
                
                if minLength == 1:
                    return minLength
                
                while j < len(nums) and windowSum < target:
                    j += 1
                    if j < len(nums):
                        windowSum += nums[j]

                if windowSum >= target:
                    minLength = min(minLength, j - i + 1)

                while i < j and windowSum >= target:
                    windowSum -= nums[i]
                    i += 1
                    if windowSum >= target:
                        minLength = min(minLength, j - i + 1)
                        
            if minLength == 10**9:
                return 0
            return minLength
        