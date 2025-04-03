class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        pref = [nums[0]]
        suf = [nums[-1]]
        ans = 0

        for i in range(1, n):
            pref.append(max(pref[-1], nums[i]))

        for i in range(n - 2, -1, -1):
            suf.append(max(suf[-1], nums[i]))

        suf = suf[::-1]

        for i in range(1, n - 1):
            best = (pref[i - 1] - nums[i]) * suf[i + 1]
            ans = max(ans, best)

        return ans