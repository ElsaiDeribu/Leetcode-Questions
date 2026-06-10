class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_chrs = [0] * 26
        t_chrs = [0] * 26

        for character in s:
            s_chrs[ord(character) - 97] += 1

        for character in t:
            t_chrs[ord(character) - 97] += 1
        

        return s_chrs == t_chrs
        