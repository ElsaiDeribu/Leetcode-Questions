class Solution:
    def minWindow(self, s: str, t: str) -> str:


        window = defaultdict(int)
        t = Counter(t)
        ans = float("inf")
        left, right = None, None
        l = 0

        def is_valid():
            for key, val in t.items():
                if window[key] < val:
                    return False
            return True


        for r in range(len(s)):

            window[s[r]] += 1
            while is_valid():
                if r - l + 1 < ans:
                    ans = r - l + 1
                    left, right = l, r

                window[s[l]] -= 1
                l += 1

        
        return s[left:right + 1] if left != None else ""


        