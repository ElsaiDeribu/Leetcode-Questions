class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = Counter(words[0])

        for i in range(1, len(words)):
            
            count = Counter(words[i])
            
            for c in common:
                if c in count:
                    common[c] = min(common[c], count[c])
                else:
                    common[c] = 0

        ans = [c for c in common for _ in range(common[c])]

        return ans

