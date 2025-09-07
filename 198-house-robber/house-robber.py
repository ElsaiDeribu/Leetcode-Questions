class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dp(curr):

            if curr >= len(nums):
                return 0


            # take
            res1 = dp(curr + 2) + nums[curr]

            # not take
            res2 = dp(curr + 1)

            return max(res1, res2)


        return dp(0)
