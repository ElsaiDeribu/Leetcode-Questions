class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        largest = 0

        for i, n in enumerate(nums):

            largest = max(largest, n)
            if i != len(nums) - 1 and largest == 0:
                return False
            largest -= 1

        return True
    