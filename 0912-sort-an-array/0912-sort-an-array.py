class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        heap = []
        ans = []
        
        for i in nums:
            heappush(heap, i)
            
        while heap:
            ans.append(heappop(heap))
            
        return ans