class SmallestInfiniteSet:

    def __init__(self):
        self.nums = []
        self.curr = 1
        self.added = set()
        

    def popSmallest(self) -> int:

        if self.nums:
            self.added.remove(self.nums[0])
            return heappop(self.nums)

        res = self.curr
        self.curr += 1
        return res
        

    def addBack(self, num: int) -> None:
        
        if num < self.curr and num not in self.added:
            self.added.add(num)
            heappush(self.nums, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)