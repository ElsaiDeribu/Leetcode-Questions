class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        @cache
        def dp(w1, w2):
            if w1 == len(word1):
                return len(word2) - w2

            if w2 == len(word2):
                return len(word1) - w1

            if word1[w1] == word2[w2]:
                return dp(w1 + 1, w2 + 1) 

            return 1 + min(
                dp(w1, w2 + 1), # insert
                dp(w1 + 1, w2), # delete
                dp(w1 + 1, w2 + 1) # replace
                )


        return dp(0,0)