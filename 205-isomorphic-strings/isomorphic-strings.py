class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic_s= defaultdict(str)
        dic_t = defaultdict(str)



        for i in range(len(s)):
            if (s[i] in dic_s and dic_s[s[i]] != t[i]) or (t[i] in dic_t and dic_t[t[i]] != s[i]):
                return False

            else:
                dic_s[s[i]] = t[i]
                dic_t[t[i]] = s[i]


        return True