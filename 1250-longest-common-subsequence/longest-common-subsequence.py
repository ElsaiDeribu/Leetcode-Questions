class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        @cache
        def dp(l, r):
            if l == len(text1) or r == len(text2):
                return 0

            if text1[l] == text2[r]:
                return dp(l + 1, r + 1) + 1

            else:
                res1 = dp(l + 1, r)
                res2 = dp(l, r + 1)

                return max(res1, res2)


        return dp(0, 0)

            
        