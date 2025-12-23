class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        def rob(start, end):
            prev2, prev1 = 0, 0

            for i in range(start, end):
                num = nums[i]
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1


        return max(rob(0, len(nums) - 1), rob(1, len(nums)))



        