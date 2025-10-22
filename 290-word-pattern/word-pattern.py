class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        dic_p = defaultdict(str)
        dic_s = defaultdict(str)

        if len(pattern) != len(s):
            return False

        l, r = 0, 0

        while l < len(pattern) and r < len(s):

            if (dic_p[pattern[l]] and dic_p[pattern[l]] != s[r] ) or (dic_s[s[r]] and pattern[l] != dic_s[s[r]]):
                return False

            dic_p[pattern[l]] = s[r]
            dic_s[s[r]] = pattern[l]

            l += 1
            r += 1

        return True



        