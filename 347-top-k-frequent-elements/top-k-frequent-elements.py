class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # TC: O(nlogk)
        # SC: O(n)

        count = Counter(nums)
        heap = []
        ans = []

        for num, freq in count.items():
            heappush(heap, (freq, num))

            if len(heap) > k:
                heappop(heap)


        return [num for freq, num in heap]





        