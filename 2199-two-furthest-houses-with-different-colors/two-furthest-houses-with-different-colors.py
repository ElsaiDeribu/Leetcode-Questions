class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        

        ans= 0

        for i in range(len(colors)):
            for j in range(i):
                if not colors[i] == colors[j]:
                    ans = max(ans, abs(j - i))

        return ans