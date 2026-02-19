class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1

            else:
                r = m
        
        if l < len(nums) and nums[l] == target:
            return l

        return -1
    