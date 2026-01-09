class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # TC:O(n²)
        # SC:O(n)

        wordDict = set(wordDict)

        @cache
        def dp(idx):
            if idx >= len(s):
                return True

            for i in range(idx, len(s)):
                if s[idx:i + 1] in wordDict and dp(i + 1):
                    return True

            return False
                

        return dp(0)