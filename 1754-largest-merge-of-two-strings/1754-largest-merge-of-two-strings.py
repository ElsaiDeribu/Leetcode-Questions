class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        ans = ''
        
        while word1 or word2:
            if word1 > word2:
                ans += word1[0]
                word1 = word1[1:]
            else:
                ans += word2[0]
                word2 = word2[1:]
        
        return ans
