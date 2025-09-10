class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        words = sorted(Counter(words).items(), key = lambda x: (-x[1], x[0]) )

        return [words[i][0] for i in range(k)]
        

