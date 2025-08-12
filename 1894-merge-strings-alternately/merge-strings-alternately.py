class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []
        p1, p2 = 0, 0

        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                res.append(word1[p1])
                p1 += 1

            if p2 < len(word2):
                res.append(word2[p2])
                p2 += 1

        return ''.join(res)


        