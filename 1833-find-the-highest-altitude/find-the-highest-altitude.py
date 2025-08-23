class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        curr = 0
        ans = 0

        for i in range(len(gain)):
            
            curr += gain[i]

            ans = max(ans, curr)

        return ans

        