class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        last = ""
        ans = []

        for idx, val in enumerate(words):
            anag = sorted(Counter(val).items())

            if not anag == last:
                ans.append(val)
                last = anag


        return ans

                
        