class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not len(s) == len(t):
            return False

        s_count = [0] * 26
        t_count = [0] * 26

        for i in range(len(s)):
            
            s_count[ord(s[i]) - 97] += 1
            t_count[ord(t[i]) - 97] += 1


        return s_count == t_count
        