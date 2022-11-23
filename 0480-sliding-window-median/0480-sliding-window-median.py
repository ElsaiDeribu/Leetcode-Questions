class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap = []
        maxHeap = []
        ans = []
        l = 0
        
        for r in range(len(nums)):
            if r - l + 1 > k:
                if maxHeap and nums[l] <= -maxHeap[0]:
                    maxHeap.pop(maxHeap.index(-nums[l]))
                    heapify(maxHeap)
                else:
                    minHeap.pop(minHeap.index(nums[l]))
                    heapify(minHeap)
                l += 1
                
            if len(maxHeap) >= len(minHeap):
                heappush(maxHeap, -nums[r] )
                heappush(minHeap, -heappop(maxHeap))
            else:
                heappush(minHeap, nums[r])
                heappush(maxHeap, -heappop(minHeap))
                
            if r - l + 1 == k:
                if len(maxHeap) == len(minHeap):
                    ans.append((-maxHeap[0] + minHeap[0])/2 )
                elif len(maxHeap) > len(minHeap):
                    ans.append(-maxHeap[0])
                else:
                    ans.append(minHeap[0])
            
        return ans
                
                

            