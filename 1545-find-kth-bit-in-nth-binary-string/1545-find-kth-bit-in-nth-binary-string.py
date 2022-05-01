class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        def recurence(n, k, s):
            if n == 0:
                return s[k - 1]
            n -= 1
            s = s + "1" + invert(s)[::-1]
            
            return recurence(n, k, s)
        
        def invert(s):
            inverted = ""
            for i in s:
                if i == "0":
                    inverted += "1"
                else:
                    inverted += "0"
            return inverted
        return recurence(n, k, s)