class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # TC: O(n²)
        # SC: O(n)

        n = len(nums)

        @cache
        def dfs(idx):
            if idx >= n - 1:
                return 0

            res = float("inf")
            left = idx + 1
            right = idx + nums[idx]

            for i in range(left, right + 1):
                res = min(res, dfs(i))

            return res + 1


        return dfs(0) 