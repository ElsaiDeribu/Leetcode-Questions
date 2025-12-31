class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # TC:O(n²)
        # SC:O(n)

        wordDict = set(wordDict)

        @cache
        def dp(idx):
            if idx >= len(s):
                return True

            res = False
            for i in range(idx, len(s)):
                if s[idx:i + 1] in wordDict:
                    res = res or dp(i + 1)

            return res
                

        return dp(0)