class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        ans = []
        
        for i in range(len(nums2)):
            
            total = nums1[0]+ nums2[i]
            heappush(heap,(total, (0, i)))
            
            
        while k and heap:
            
            smallest = heappop(heap)[1]
            n1 = smallest[0]
            n2 = smallest[1]
            
            ans.append([nums1[n1], nums2[n2]])
            nxt = n1 + 1
            
            if nxt < len(nums1):
                total = nums1[nxt] + nums2[n2]
                heappush(heap, (total, (nxt, n2)))
            
            k -= 1
            
        return ans