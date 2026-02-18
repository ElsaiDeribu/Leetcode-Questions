class Solution:
    def almostPalindromic(self, s: str) -> int:


        def check(l, r, can_skip):


            while l >= 0 or r < len(s):

                if l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

                elif can_skip:
                    skip_left = check(l - 1, r, False)
                    skip_right = check(l, r + 1, False)

                    return max(skip_left, skip_right)

                else:
                    break


            return r - l - 1



        ans = 0

        for i in range(len(s)):
            odd = check(i, i, True)
            even = check(i, i + 1, True)
            
            ans = max(odd, even, ans)

        return ans

         