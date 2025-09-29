class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic_s, dic_t= defaultdict(str), defaultdict(str)

        for a, b in zip(s, t):
            if (a in dic_s and dic_s[a] != b) or (b in dic_t and dic_t[b] != a):
                return False

            dic_s[a] = b
            dic_t[b] = a


        return True