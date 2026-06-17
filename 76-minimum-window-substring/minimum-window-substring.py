class Solution:
    def minWindow(self, s: str, t: str) -> str:


        window = defaultdict(int)
        t = Counter(t)
        ans = float("inf")
        left, right = None, None
        have = 0
        need = len(t)
        l = 0

        for r in range(len(s)):

            window[s[r]] += 1

            if window[s[r]] == t[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < ans:
                    ans = r - l + 1
                    left, right = l, r

                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < t[s[l]]:
                    have -= 1
                    
                l += 1

        
        return s[left:right + 1] if left != None else ""


        