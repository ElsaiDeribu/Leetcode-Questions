class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        ans = float("-inf")

        while l < r:

            h = min(height[l], height[r])
            w = r - l

            ans = max(ans, h * w)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return ans

        