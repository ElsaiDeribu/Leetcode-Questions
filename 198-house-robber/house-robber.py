class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dp(curr, res):

            if curr >= len(nums):
                return res


            # take
            res1 = dp(curr + 2, res + nums[curr])

            # not take
            res2 = dp(curr + 1, res)

            return max(res1, res2)


        return dp(0,0)
