class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        cache = [0] * n

        for i in range(n - 1, -1, -1):
            
            next_h = i + 2

            rob = nums[i] + (cache[next_h] if next_h < n else 0)
            not_rob = cache[i + 1] if i + 1 < n else 0

            cache[i] = max(rob, not_rob)

        return cache[0]
        