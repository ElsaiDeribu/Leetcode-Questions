class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_str = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(s)):
            window_str[s[r]] += 1

            while window_str[s[r]] > 1:
                window_str[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans