class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x + 1

        while l + 1 < r:
            mid = l + (r - l) // 2

            if mid * mid > x:
                r = mid
            else:
                l = mid 


        return l
        