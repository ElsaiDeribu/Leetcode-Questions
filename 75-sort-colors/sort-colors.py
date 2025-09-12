class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        # count colors
        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1

        # sort or replace colors in order
        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red -= 1

            elif white:
                nums[i] = 1
                white -= 1

            else:
                nums[i] = 2
                blue -= 1
        