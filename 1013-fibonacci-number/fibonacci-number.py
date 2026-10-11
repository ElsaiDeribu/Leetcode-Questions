class Solution:
    def fib(self, n: int) -> int:

        # TC: O(n)
        # SC; O(1)

        if n == 0: return 0
        if n == 1: return 1
        
        a, b = 0, 1

        for _ in range(n - 1):
            c = a + b
            a = b
            b = c


        return b
            

