class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        kThLargest = 0
        for i in nums:
            heappush(heap, -i)
            
        while k:
            kThLargest = -heappop(heap)
            k -= 1
            
        return kThLargest