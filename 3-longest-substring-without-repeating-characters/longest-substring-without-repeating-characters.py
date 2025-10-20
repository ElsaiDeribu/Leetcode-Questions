class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        win = set()
        ans = float("-inf")
        l = 0

        for r in range(len(s)):

            while s[r] in win:
                if s[l] in win:
                    win.remove(s[l])
                l += 1

            win.add(s[r])

            ans = max( ans, r - l + 1)

        return ans if s else 0
        