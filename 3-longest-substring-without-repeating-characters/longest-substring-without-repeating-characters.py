class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        win = set()
        l, ans = 0, 0

        for r in range(len(s)):

            while s[r] in win:
                win.remove(s[l])
                l += 1

            win.add(s[r])

            ans = max( ans, r - l + 1)

        return ans
        