class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ans = 0
        n = max(a.bit_length(), b.bit_length(), c.bit_length())
        
        for i in range(n):
            b1 = (a >> i) & 1
            b2 = (b >> i) & 1
            b3 = (c >> i) & 1

            if (b1 | b2) != b3:
                if b3 == 1:
                    ans += 1

                else:
                    if b1 == b2 == 1:
                        ans += 2
                    else:
                        ans += 1


        print(bin(a), bin(b), bin(c))
        return ans