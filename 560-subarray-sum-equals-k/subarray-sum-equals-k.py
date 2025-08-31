class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)
        dic[0] = 1

        total = 0
        ans = 0

        for i in range(len(nums)):

            total += nums[i]

            req = total - k

            ans += dic[req]

            dic[total] += 1

        return ans

        