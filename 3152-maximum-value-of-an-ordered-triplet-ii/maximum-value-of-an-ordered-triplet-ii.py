class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        pref = nums[:]
        suf = nums[:]
        ans = 0

        for i in range(1, n):
            pref[i] = max(pref[i], pref[i - 1])
            suf[n - i - 1] = max(suf[n - i - 1], suf[n - i])

        for i in range(1, n - 1):
            best = (pref[i - 1] - nums[i]) * suf[i + 1]
            ans = max(ans, best)

        return ans