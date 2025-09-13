class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels =  {'a', 'e', 'i', 'o', 'u'}
        freq = [0] * 26
        max_vowel = 0
        max_cons = 0

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1

            if ch in vowels:
                max_vowel = max(max_vowel, freq[idx])
            else:
                max_cons = max(max_cons, freq[idx])

        return max_vowel + max_cons
