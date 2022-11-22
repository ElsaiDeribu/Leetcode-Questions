class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) >= len(self.minHeap):
            heappush(self.maxHeap, -num)
            heappush(self.minHeap, -heappop(self.maxHeap))
        else:
            heappush(self.minHeap, num)
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            median = (self.minHeap[0] - self.maxHeap[0]) / 2
            return median
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()