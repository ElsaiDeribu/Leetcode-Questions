class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums = sorted(zip(nums2, nums1), reverse = True)
        hp = []
        total = 0
        ans = 0

        for n2, n1 in nums:
            total += n1
            heapq.heappush(hp, n1)

            if len(hp) > k:
               val =  heapq.heappop(hp)
               total -= val
\
            if len(hp) == k:
                ans = max(ans, total * n2)

        return ans