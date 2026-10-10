class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        l = 0
        window = set()

        for r in range(len(s)):

            while s[r] in window: 
                window.remove(s[l])
                l += 1

            window.add(s[r])

            ans = max(r - l + 1, ans)


        return ans