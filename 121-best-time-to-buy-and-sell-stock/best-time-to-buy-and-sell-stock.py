class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = float("inf")
        ans = float("-inf")

        for num in prices:
            smallest = min(smallest, num)
            ans = max(ans, num - smallest)


        return ans



      