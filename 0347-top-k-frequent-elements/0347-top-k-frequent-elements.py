class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = []
        ans = []
        
        for i in count:
            heappush(heap, (-count[i], i))
            
        
        while k:
            ans.append(heappop(heap)[1])
            k -= 1
            
        return ans
        