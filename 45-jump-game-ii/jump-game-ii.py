class Solution:
    def jump(self, nums: List[int]) -> int:
        

        l, r = 0, 0
        ans = 0

        while r < len(nums) - 1:

            max_dest = 0
            for i in range(l, r + 1):
                max_dest = max(max_dest, i + nums[i])

            ans += 1
            l = r + 1
            r = max_dest

        return ans
