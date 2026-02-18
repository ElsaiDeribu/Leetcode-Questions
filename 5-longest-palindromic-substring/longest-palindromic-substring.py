class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def check(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l, r

        
        ans = [-1, 1]
        longest = 1

        for i in range(len(s)):
            odd = check(i, i)
            even = check(i, i + 1)

            if odd[1] - odd[0] - 1 > longest:
                ans = odd[0], odd[1]
                longest = odd[1] - odd[0] - 1

            if even[1] - even[0] - 1 > longest:
                ans = even[0], even[1]
                longest = even[1] - even[0] - 1 

        return s[ans[0] + 1:ans[1]]



        