class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def tri(curr):

            if curr == 0:
                return 0

            if curr in [1,2]:
                return 1

            return tri(curr - 3) + tri(curr - 2) + tri(curr - 1)

        return tri(n)
        