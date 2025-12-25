class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Time Complexity: O(amount × len(coins))
        # Space Complexity: O(amount)

        @cache
        def dp(rem):
            if rem == 0:
                return 0

            if rem < 0:
                return float("inf")

            res = float("inf")
            for c in coins:
                res = min(res, dp(rem - c))

            return res + 1


        ans = dp(amount)

        return -1 if ans == float("inf") else ans