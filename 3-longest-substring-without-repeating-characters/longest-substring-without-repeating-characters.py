class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        l = 0
        window_dic = defaultdict(int)


        for r in range(len(s)):
            window_dic[s[r]] += 1

            while window_dic[s[r]] > 1:
                window_dic[s[l]] -= 1
                if window_dic[s[l]] == 0:
                    window_dic.pop(s[l])

                l += 1

            ans = max(len(window_dic), ans)


        return ans

            



