class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 0

        while r < len(nums):

            if nums[r] == 0:
                r += 1
                continue

            nums[l], nums[r] = nums[r], nums[l]
            r += 1
            l += 1


