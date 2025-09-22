class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        count = Counter(nums)

        count = list(sorted(count.items(), key = lambda x: x[1], reverse=True))

        ans = count[0][1]

        for i in range(1, len(count)):
            if count[i][1] == count[0][1]:
                ans += count[i][1]

        return ans