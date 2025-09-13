class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels =  'a', 'e', 'i', 'o', 'u'

        max_vowel = 0
        max_cons = 0
        count = Counter(s)

        for key, val in count.items():
            if key in vowels:
                max_vowel = max(max_vowel, val)
            else:
                max_cons = max(max_cons, val)

        return max_vowel + max_cons
