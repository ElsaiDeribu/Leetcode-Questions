class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        cache = [-1] * n

        def backtrack(i):
            if i >= n:
                return 0

            if cache[i] != -1:
                return cache[i]

            take = nums[i] + backtrack(i + 2)
            not_take = backtrack(i + 1)

            cache[i] = max(take, not_take)

            return cache[i]

        return backtrack(0)
        