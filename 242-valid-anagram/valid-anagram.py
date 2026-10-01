class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        S = [0] * 26
        T = [0] * 26

        for char in s:
            S[ord(char) - 97] += 1

        for char in t:
            T[ord(char) - 97] += 1
        
        return S == T