class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()

        ans = 0

        for val in range(1001):
            idx = bisect_left(citations, val)

            if len(citations) - idx >= val:
                ans = val


        return ans
        