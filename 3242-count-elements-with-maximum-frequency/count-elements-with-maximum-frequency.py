class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        count = Counter(nums)

        largest = max(count.values())

        count = Counter(count.values())

        return largest * count[largest]