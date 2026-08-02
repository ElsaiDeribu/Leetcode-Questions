class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(idx, last_action):
            if idx == len(prices): return 0

            if last_action == "buy":
                res1 = dfs(idx + 1, last_action)
                res2 = dfs(idx + 1, "sell") + prices[idx]

                return max(res1, res2)

            else:
                res1 = dfs(idx + 1, last_action)
                res2 = dfs(idx + 1, "buy") - prices[idx]

                return max(res1, res2)


        return dfs(0, "")
