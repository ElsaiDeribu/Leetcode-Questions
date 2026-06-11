class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_str = set()
        ans = 0
        l = 0

        for r in range(len(s)):

            while s[r] in window_str:
                window_str.remove(s[l])
                l += 1

            window_str.add(s[r])
            ans = max(ans, r - l + 1)

        return ans