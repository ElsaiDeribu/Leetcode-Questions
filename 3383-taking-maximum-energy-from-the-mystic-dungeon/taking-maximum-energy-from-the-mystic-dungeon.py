class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:



        @cache
        def dp(idx):
            if idx >= len(energy):
                return 0

            return dp(idx + k) + energy[idx]


        ans = float("-inf")

        for i in range(len(energy)):
            ans = max(ans, dp(i))

        return ans
        