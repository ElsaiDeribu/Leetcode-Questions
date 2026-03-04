class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)

        while l < r:
            
            m = (l + r) // 2

            if m + 1 < len(nums) and nums[m] < nums[m + 1]:
                l = m + 1

            else:
                r = m

        return l