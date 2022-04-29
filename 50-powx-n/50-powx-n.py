class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        n -= 1
        return x * pow(x, n)
        