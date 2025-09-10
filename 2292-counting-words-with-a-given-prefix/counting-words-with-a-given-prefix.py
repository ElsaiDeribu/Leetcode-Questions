class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        words.sort()
        lo = bisect.bisect_left(words, pref)
        hi = bisect.bisect_left(words, pref + '{')
        return hi - lo