class Solution:
    def trailingZeroes(self, n: int) -> int:
        # TC: O(log_5 n)  - n divided by 5 each iteration
        # SC: O(1)        - only constant extra space used

        ans = 0

        while n:
            ans += n // 5
            n //= 5

        return ans
