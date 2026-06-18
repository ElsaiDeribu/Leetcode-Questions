class Solution:
    def minWindow(self, s: str, t: str) -> str:


        window = defaultdict(int)
        t = Counter(t)
        have, need = 0, len(t)
        left, right = None, None
        l = 0


        for r in range(len(s)):

            window[s[r]] += 1
            if window[s[r]] == t[s[r]]:
                have += 1

            while have == need:
                if (left == None) or r - l < right - left:
                    left, right  = l, r

                window[s[l]] -= 1
                if window[s[l]] < t[s[l]]:
                    have -= 1
                l += 1

        return s[left: right + 1] if left != None else ""



        

        