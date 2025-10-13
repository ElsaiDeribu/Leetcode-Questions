class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        last = ""
        l = 0

        for idx, val in enumerate(words):
            anag = sorted(Counter(val).items())

            if not anag == last:
                words[l] = val
                last = anag
                l += 1


        return words[:l]

                
        