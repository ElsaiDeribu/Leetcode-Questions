class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        l = 0
        window = defaultdict(int)
      

        for r in range(len(s)):
            window[s[r]] += 1

            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)


        return ans
        