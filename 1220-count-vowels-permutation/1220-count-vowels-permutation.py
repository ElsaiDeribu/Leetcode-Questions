class Solution:
    def countVowelPermutation(self, n: int) -> int:
        

        @cache
        def dp(prev, n):
            if n == 0:
                return 1
            
            if prev == "a":
                res = dp("e", n - 1 )
                return res
                
            elif prev == "e":
                res1 = dp("a", n - 1)
                res2 = dp("i", n - 1)
                return res1 + res2
                
            elif prev == "i":
                res1 = dp("a", n - 1)
                res2 = dp("e", n - 1)
                res3 = dp("o", n - 1)
                res4 = dp("u", n - 1)
                return res1 + res2 + res3 + res4
                
            elif prev == 'o':
                res1 = dp("i", n - 1)
                res2 = dp("u", n - 1)
                return res1 + res2
                
            elif prev == "u":
                res = dp("a", n - 1)
                return res
                
        ans = 0
        mod = 10 ** 9 + 7
        
        for vowl in ['a', 'e', 'i', 'o', 'u']:
            ans += dp(vowl, n - 1)
            ans %= mod
            
        mod = 10 ** 9 + 7
            
        return ans
            
        